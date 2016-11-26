#coding=utf-8
class jParser(object):
    def __init__(self, text, items):
        self.text = text
        self.items = items
    
    def parse(self):
        # Get text
        text = self.text
        # Initialize values
        isCode = False
        code = ""
        output = ""
        pointer = 0
        length = len(text)
        text += " "# To avoid data overflow.
        while True:
            # Common text
            if not isCode and text[pointer] != "{" and text[pointer+1] != "{" :
                output += text[pointer]
            # Code begin
            elif text[pointer] == "{" and text[pointer+1] == "{":
                pointer += 1
                isCode = True
                code = ""
            # Code end
            elif isCode and text[pointer] == "}" and text[pointer+1] == "}":
                pointer += 1
                isCode = False
                # Parse code (return operations)
                operation = {}
                operation = self.codeParser(code)
                # Get command
                command = operation.get("command")
                # Solve command
                # Command common
                if command == "common":
                    try:
                        output += operation.get("detail")
                    except:
                        pass

                # Command for
                elif command == "for":
                    # Dim for layer
                    forLayer = 1
                    # Dim the offset where the loop block start
                    startPointer = pointer
                    # Dim a pointer to loop
                    forPointer = pointer
                    # Find the complete loop block
                    while forLayer:
                        if text[forPointer:forPointer+6] == "{{ for":
                            forLayer += 1
                        elif text[forPointer:forPointer+13] == "{{ end for }}":
                            forLayer -= 1
                        if forPointer >= length:
                            break
                        forPointer += 1
                    # Get code block content 
                    codeBlock = text[startPointer+1:forPointer]

                    # Begin loop 
                    start = operation["start"]
                    while start <= operation["end"]:
                        # Recursion
                        temp = jParser(codeBlock, self.items)
                        output += temp.parse()
                        start += operation["step"]

                    # Adjust global offset
                    pointer = forPointer + 12

                # Command default
                elif command == "error":
                    pass
                # Command end
            elif isCode:
                code += text[pointer]
        
            pointer += 1
            if pointer == length:
                break
        return output
    
    def codeParser(self, code):
        # Initialize return data
        result = {}
        # Split source data
        data = code.split()

        # Case for
        if data[0] == "for" and data[2] == "to":
            result["command"] = "for"
            # Get start
            if data[1][0] == "$":
                result["start"] = float(self.items.get(data[1].replace("$", "")))
            else:
                result["start"] = float(data[1])
            # Get end
            if data[3][0] == "$":
                result["end"] = self.items.get(data[3].replace("$", ""))
            else:
                result["end"] = float(data[3])
            # Get step
            try:
                if data[5][0] == "$":
                    result["step"] = float(self.items.get(data[5].replace("$", "")))
                else:
                    result["step"] = float(data[5])
            except:
                result["step"] = 1
            return result

            

        # Case if
        elif data[0] == "if":
            pass

        # Case common ( All data are printed as value ).
        elif data[0][0] == "$":
            # Check if each data is legal.
            for d in data:
                if d[0] != "$":
                    # If is illegal, return ERROR.
                    result["command"] = "error"
                    return result
            result["command"] = "common"
            # Reset or announce detail
            detail = []
            # Get values
            for d in data:
                detail.append(self.items.get(d.replace("$", "")))
            try:
                result["detail"] = " ".join(detail)
            # If the list have only one item, join will return an error. 
            except:
                result["detail"] = detail[0]
            return result

        # Case default
        else:
            result["command"] = "error"
            return result