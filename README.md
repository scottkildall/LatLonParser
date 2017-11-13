##LatLonParser
####Written by Scott Kildall
####November 13 2017



##Description
Many datasets will have a column of lat/lon data written out as: (37.8007983983, -122.4368696024)

This isn't very useful for custom mapping code, so this will strip out the parenthesis and get it into a more useful format.

Specifically it will convert Either

- "(37.8007983983, -122.4368696024)" to 37.8007983983, -122.4368696024
- (37.8007983983, -122.4368696024) to 37.8007983983, -122.4368696024

That's all this script does!



### Input file
Looks for an input file named **input.csv**.

The format rules are as follows:

(1) It may contain a header (1st row)or not. If the 1st row has no comma in it, it will ignore this

(2) Every other row must have two numbers in it with a comma and parentheses. It may or may not include quotation marks in it, i.e.

(37.8007983983, -122.4368696024)

OR

"(37.8007983983, -122.4368696024)"

Are both valid

(3) Any data past the right parenthesis will be completely ignored.

### Output file

(1) If there is a header in the input file, the output file will include the headers with the names Latitude and Longitude. Latitude will be always first.

(2) If no header in the input file, there will be no header in the output file


