plate_name = 'plate077i'

induced = 1

growth_file = plate_name + "_600.txt"
miller_csv = plate_name + "_420.txt"
optics_csv = plate_name + "_550.txt"

raw_growth = "2017_11_29_crpocl_campconcs_plate3_inducedfull_OD600_3h.txt"
raw_miller = "2017_11_29_crpocl_campconcs_plate3_inducedfull_miller_10h_420.txt"
raw_optics = "2017_11_29_crpocl_campconcs_plate3_inducedfull_miller_10h_550.txt"

num_rows = 8
num_cols = 12
date = '17.11.29'

stop_time = 600
start_time = 0

cultures_dict = {
	0:'RDM',
	1:'b1A5',
	2:'b5A5',
	3:'b5B2',
	4:'b5B3',
	5:'b5B8',
	6:'b5B9',
	7:'b5C3',
	8:'b5C5',
	9:'b5D1',
	10:'b5E4',
	11:'b5F2',
	12:'b5F3',
	13:'b5F5',
	14:'b5F6',
	15:'b5G4',
	16:'b5G9',
	17:'b5H1',
	18:'b5H2',
	19:'b5H3',
	20:'b5H4',
	21:'b5H5',
	22:'b5H6',
	23:'b5H7',
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

camp_concentrations_string_u = '''
0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0
'''

camp_concentrations_string_i = '''
250	250	250	250	250	250	250	250	250	250	250	250
250	250	250	250	250	250	250	250	250	250	250	250
250	250	250	250	250	250	250	250	250	250	250	250
250	250	250	250	250	250	250	250	250	250	250	250
250	250	250	250	250	250	250	250	250	250	250	250
250	250	250	250	250	250	250	250	250	250	250	250
250	250	250	250	250	250	250	250	250	250	250	250
250	250	250	250	250	250	250	250	250	250	250	250
'''

camp_concentrations_string_h = '''
125	125	125	125	125	125	125	125	125	125	125	125
125	125	125	125	125	125	125	125	125	125	125	125
125	125	125	125	125	125	125	125	125	125	125	125
125	125	125	125	125	125	125	125	125	125	125	125
125	125	125	125	125	125	125	125	125	125	125	125
125	125	125	125	125	125	125	125	125	125	125	125
125	125	125	125	125	125	125	125	125	125	125	125
125	125	125	125	125	125	125	125	125	125	125	125
'''

if induced==1: camp_concentrations_string = camp_concentrations_string_i
elif induced==2: camp_concentrations_string = camp_concentrations_string_u
elif induced==3: camp_concentrations_string = camp_concentrations_string_h

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
