## Values

{{ $valuesName }}
{{ $valuesName1 $valuesName2 }}

## If

{{ if $i == $j }}
{{ do something }}
{{ end if }}

The application will compare the two value by transform them to string when using "=="

## For

{{ for $i to $name step 1 }}   (step default 1)
{{ do something }}
{{ end for }}

