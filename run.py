from functools  import partial

# def is_good_read(position, quality_score, (_id, _seq, _delim, qualities)):
def is_good_read(position, quality_score, read):
    _, _, _, qualities = read
    return qualities[position] > quality_score
 
filter_reads = partial(filter, partial(is_good_read, 10, 20)) 
   
#def filter_reads(reads):
    #return filter(partial(is_good_read, 10, 20), reads);
    ##return filter(lambda r: is_good_read(10, 20, r), reads);
    
    ### good_reads = []
    ### for r in reads:
    ###     if is_good_read(10, 20, r):
    ###         good_reads.append(r)
    ### return good_reads