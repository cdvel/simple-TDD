from nose.tools import *
from run import *

good = [	'@id',
	    'ATCGCGCGGATCCC',
	    '+',
	    [40, 40, 40, 40, 40, 40, 40, 44, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40]
	];
    
bad = [	'@id',
	    'ATCGCGCGGATCCC',
	    '+',
	    [15, 15, 15, 10, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
	];

def test_is_read_good():
    assert_true(is_good_read(10, 20, good))    
    assert_false(is_good_read(10, 20, bad))
    
def test_filter_reads():
    assert_equals([good, good, good], filter_reads([good, good, good]));
    assert_not_equals([good, bad, good], filter_reads([good, good]));
    assert_equals([good, bad, good, good], filter_reads([good, good])); 
