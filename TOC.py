import pymupdf
import argparse
import os

def validateFiles(filename, input_file, check_input):
    if not os.path.exists(filename):
        print("PDF File does not exist")
        return False
    if not filename.lower().endswith(".pdf"):
        print("PDF file must be pdf")
        return False
      
    if check_input and not os.path.exists(input_file):
        print("Input file does not exist")
        return False
    
    return True
        
def updatePdfToc(filename, input_file, shift, remove, output):
    with open(filename, 'rb' ) as file:
        print("Running\n")
        pdf_reader = pymupdf.open(file)
        
        toc = []
        if not remove:
             toc += pdf_reader.get_toc()
        
        
        with open(input_file, 'r' , encoding='utf-8') as input_data:
            for line in input_data:
                count = 0
                for c in line:
                    if (c == '>'):
                        count += 1
                    else:
                        break
                
                if count == 0: 
                    continue
                    
                remainingLine = line[count:].lstrip().rstrip()
                remainingLineParts = remainingLine.split('|')
                print(remainingLineParts)
                toc.append([count,remainingLineParts[0].lstrip().rstrip()
                ,int(remainingLineParts[1])+shift])
        
        
        sortedToc = sorted(toc, key= lambda val : val[2])
        pdf_reader.set_toc(sortedToc)    

        if (output == None):
            pdf_reader.save(filename, incremental=True, encryption=pymupdf.PDF_ENCRYPT_KEEP)
        elif (output == filename):
            pdf_reader.save(output, incremental=True, encryption=pymupdf.PDF_ENCRYPT_KEEP)
        else:
            pdf_reader.save(output)
        
    print("\nFinished")
    
def writeInputData(filename, output_file):
    pdf_reader = pymupdf.open(filename) 
    with open(output_file, 'w' , encoding='utf-8') as file:
        toc = pdf_reader.get_toc()
        for i in toc:
            outline_string = '>'*i[0] + i[1]+','+str(i[2]) +'\n'
            file.write(outline_string)
            
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
         prog='TOC Creator',
         description='Create table of contents for pdf files',
        )
    parser.add_argument('file_path', help="Path for pdf file")    
    parser.add_argument('-i', '--input', required=True, 
        help="Path for input table of contents data file")
    parser.add_argument('-s', '--offset', 
        help="Amount to offset page numbers by", default = 0, type=int)
    parser.add_argument('-r', '--remove', action="store_true",
        help = "Removes previous table of content")
    parser.add_argument('-o', '--output', 
        help="Output file location. Overwrites input file if not set")
    parser.add_argument('-d', '--display', action="store_true", 
        help="""Stores current table of contents as input data in the file specified by
        -i. Does not update TOC.""")

    args = parser.parse_args()
    if (validateFiles(args.file_path, args.input, not args.display)):
        if (args.display):
            writeInputData(args.file_path, args.input)
        else:
            updatePdfToc(args.file_path, args.input, args.offset, args.remove,args.output)