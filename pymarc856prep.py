from pymarc import MARCReader
from pymarc import Record, Field 

#this script preps ebook files for Evergreen by removing the GMD and extraneous links, adding a holdings code 
##and editing the text for the link
#you will need to specify input and output file names
#you will need to specify the holdings code for the 856$9 and link text for 856$z below

shortcode = 'WYO'
linktext = 'Click to access digital title. Please have your valid Wyomissing Public Library card handy.'

with open('INPUTFILE.mrc', 'rb') as data:
    with open('OUTPUTFILE.mrc', 'wb') as out:
        reader = MARCReader(data)
        for record in reader:
            # In this portion of the code, you have retrieved a specific record
            # You can modify the record object as much as you want and it will
            # be written immediately to the output file at the bottom of this
            # for loop.
            
            # Here, we retrieve a list of all 926 fields, loop over them, and
            # remove the 'f' subfield from each.
          
            # delete 245 $h aka GMD
            fields = record.get_fields('245')
            for field in fields:
                field.delete_subfield('h')
                
            # Insert more modifications here...
            
            #remove 856s with $3 - excerpts, samples, etc
            fields = record.get_fields('856')
            for field in fields:
                if field.get_subfields('3'):
                    record.remove_field(field)
                        
                
            #replace 856 $z
            fields = record.get_fields('856')
            for field in fields:
                field.delete_subfield('z')            
                field.add_subfield('z', linktext)
            
            #add 856$9WYO
            fields = record.get_fields('856')
            for field in fields:
                field.add_subfield('9', shortcode)

            out.write(record.as_marc())
