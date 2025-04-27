def text_splitting(text, chunk_size=500, overlap=50): #i am taking default chunk size and overlap size as 500 and 50 respectively
    chunks=[]
    start=0
    text_len=len(text)
    while start<text_len:
        end = min(start + chunk_size, text_len) #handles the cases where the text ends
        chunk=text[start:end]  #i am applying slicing technique to slice the text here
        chunks.append(chunk) #saving the newly created chunbks in the list
        start=start+(chunk_size-overlap) #getting ready for next iteration
    return chunks