#coding=utf-8
import main

testText = """
<h1> Test </h1>\n
{{ $test1 $test2 }}\n
{{ $test3 $testNone }}\n
{{ $single }}

"""
test = main.juiceTpl(testText)
test.addItem("test1", "test1")
test.addItem("test2", "TTT2")
dic = {
    "test3": "TEST333",
    "single": "SINGLE DOG"
}
test.addItems(dic)
print test.parse()