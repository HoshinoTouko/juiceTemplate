#coding=utf-8
import main

testText = """
<h1> Test </h1>\n
{{ $test1 $test2 }}

"""
test = main.juiceTpl(testText)
test.addItem("test1", "test1")
test.addItem("test2", "TTT2")
print test.parse()