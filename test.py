#coding=utf-8
import main
testText = """
{{ if 1 >= 1 }}
YES 
    {{ if $i > 1 }}
        But YES
    {{ end if }}
            {{ if 1 > 1 }}
            NO
            {{ end if }}
{{ end if }}


=============================================================
For test
{{ for 1 to $i step 3 }}
test\n
{{ for 1 to 2 }}{{ $test1 }}{{ end for }}
{{ end for }}

Common test\n
{{ $test1 $test2 }}\n
{{ $test3 $testNone }}\n
{{ $single }}

"""
test = main.juiceTpl(testText)
test.addItem("test1", "test1")
test.addItem("test2", "TTT2")
dic = {
    "test3": "TEST333",
    "single": "SINGLE DOG",
    "i": 5
}
test.addItems(dic)
print test.parse()