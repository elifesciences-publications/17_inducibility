plate_name = 'plate035u'

growth_file = plate_name + "_600.txt"
miller_csv = plate_name + "_420.txt"
optics_csv = plate_name + "_550.txt"

raw_growth = "2017.5.23_lacstar_c61r18l10lib_plate1_uninduced_315_OD600.txt"
raw_miller = "2017.5.23_lacstar_c61r18l10lib_plate1_uninduced_miller_420.txt"
raw_optics = "2017.5.23_lacstar_c61r18l10lib_plate1_uninduced_miller_550.txt"

num_rows = 8
num_cols = 12
date = '17.05.23'

stop_time = 600
start_time = 15

cultures_dict = {
	0:'RDM',
	1:'b1A5',
	2:'b1E1',
	3:'b1E2',
	4:'b2B9',
	5:'b2C1',
	6:'b2C6',
	7:'b2C7',
	8:'b2C8',
	9:'b2C9',
	10:'b2D1',
	11:'b2D2',
	12:'b2D3',
	13:'b2D4',
	14:'b2D5',
	15:'b2D6',
	16:'b2D7',
	17:'b2D8',
	18:'b2D9',
	19:'b2E1',
	20:'b2E2',
	21:'b2E3',
	22:'b2E4',
	23:'b2E5',
	24:'b1F1'
	}
	
num_strains = max(cultures_dict.keys())
	
culture_locations_string = '''
1	0	5	0	9	0	13	0	17	0	21	0
1	3	5	7	9	11	13	15	17	19	21	23
1	3	5	7	9	11	13	15	17	19	21	23
0	3	0	7	0	11	0	15	0	19	0	23
2	0	6	0	10	0	14	0	18	0	22	0
2	4	6	8	10	12	14	16	18	20	22	24
2	4	6	8	10	12	14	16	18	20	22	24
0	4	0	8	0	12	0	16	0	20	0	24
'''

camp_concentrations_string = '''
0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0
'''

culture_volumes_string = '''
50	50	50	50	50	50	50	50	50	50	50	50
50	50	50	50	50	50	50	50	50	50	50	50
50	50	50	50	50	50	50	50	50	50	50	50
50	50	50	50	50	50	50	50	50	50	50	50
50	50	50	50	50	50	50	50	50	50	50	50
50	50	50	50	50	50	50	50	50	50	50	50
50	50	50	50	50	50	50	50	50	50	50	50
50	50	50	50	50	50	50	50	50	50	50	50
'''
