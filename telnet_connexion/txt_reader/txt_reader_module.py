#!/usr/bin/python
import xlsxwriter
from datetime import datetime
import os

def txt_reader(path_to_file):
    with open(path_to_file, 'r') as file1:
        subscriber_state_information = {'IMSI': 'none',
                                        'MSISDN': 'none',
                                        'RADIO ACCESS TYPE': 'none',
                                        'PDP STATE': 'none',
                                        'TERMINAL TYPE': 'none',
                                        'LAC': 'none',
                                        'CI': 'none',
                                        'ID1': {'PDP CONTEXT ID': 'none', 'APN': 'none',
                                                'QOS PROFILE VERSION': 'none'},
                                        'ID2': {'PDP CONTEXT ID': 'none', 'APN': 'none',
                                                'QOS PROFILE VERSION': 'none'},
                                        'ID3': {'PDP CONTEXT ID': 'none', 'APN': 'none',
                                                'QOS PROFILE VERSION': 'none'},
                                        'ID4': {'PDP CONTEXT ID': 'none', 'APN': 'none',
                                                'QOS PROFILE VERSION': 'none'}
                                        }

        count = 1
        pdp_context_id = 1
        while True:
            # Get next line from file
            line = file1.readline()
            # if line is empty # end of file is reached
            if not line:
                break
            if 'UNKNOWN SUBSCRIBER' in line:
                print('ERROR: UNKNOWN SUBSCRIBER')
                break

            if 'INTERNATIONAL MOBILE SUBSCRIBER IDENTITY' in line and count == 1:
                count += 1
                # print(len(line))
                subscriber_state_information['IMSI'] = line[56:]
                print(subscriber_state_information['IMSI'])
                continue

            if 'MOBILE SUBSCRIBER INTERNATIONAL ISDN NUMBER' in line and count == 2:
                count += 1
                # print(len(line))
                subscriber_state_information['MSISDN'] = line[56:]
                print(subscriber_state_information['MSISDN'])
                continue

            if 'RADIO ACCESS TYPE' in line and count == 3:
                count += 1
                # print(len(line))
                subscriber_state_information['RADIO ACCESS TYPE'] = line[56:]
                print(subscriber_state_information['RADIO ACCESS TYPE'])
                continue

            if 'PDP STATE' in line:
                # print(len(line))
                subscriber_state_information['PDP STATE'] = line[56:]
                print(subscriber_state_information['PDP STATE'])
                continue

            if 'TERMINAL TYPE' in line:
                # print(len(line))
                subscriber_state_information['TERMINAL TYPE'] = line[56:]
                print(subscriber_state_information['TERMINAL TYPE'])
                continue

            if 'LOCATION AREA CODE' in line:
                # print(len(line))
                subscriber_state_information['LAC'] = line[56:]
                print(subscriber_state_information['LAC'])
                continue
            if 'CELL IDENTITY' in line:
                # print(len(line))
                subscriber_state_information['CI'] = line[56:]
                print(subscriber_state_information['CI'])
                continue
            if 'PDP CONTEXT ID' in line:
                # print(len(line))
                if pdp_context_id == 1:
                    subscriber_state_information['ID1']['PDP CONTEXT ID'] = line[51:]
                    print(subscriber_state_information['ID1']['PDP CONTEXT ID'])

                if pdp_context_id == 2:
                    subscriber_state_information['ID2']['PDP CONTEXT ID'] = line[51:]
                    print(subscriber_state_information['ID2']['PDP CONTEXT ID'])
                if pdp_context_id == 3:
                    subscriber_state_information['ID3']['PDP CONTEXT ID'] = line[51:]
                    print(subscriber_state_information['ID3']['PDP CONTEXT ID'])
                if pdp_context_id == 4:
                    subscriber_state_information['ID4']['PDP CONTEXT ID'] = line[51:]
                    print(subscriber_state_information['ID4']['PDP CONTEXT ID'])
                pdp_context_id += 1
                continue
            if 'QOS PROFILE VERSION' in line:
                # print(len(line))
                if pdp_context_id == 2:
                    subscriber_state_information['ID1']['QOS PROFILE VERSION'] = line[48:]
                    print(subscriber_state_information['ID1']['QOS PROFILE VERSION'])
                if pdp_context_id == 3:
                    subscriber_state_information['ID2']['QOS PROFILE VERSION'] = line[48:]
                    print(subscriber_state_information['ID2']['QOS PROFILE VERSION'])
                if pdp_context_id == 4:
                    subscriber_state_information['ID3']['QOS PROFILE VERSION'] = line[48:]
                    print(subscriber_state_information['ID3']['QOS PROFILE VERSION'])
                if pdp_context_id == 5:
                    subscriber_state_information['ID4']['QOS PROFILE VERSION'] = line[48:]
                    print(subscriber_state_information['ID4']['QOS PROFILE VERSION'])
                continue
            if 'APN ' in line:
                if pdp_context_id == 2:
                    subscriber_state_information['ID1']['APN'] = line[49:]
                    print(subscriber_state_information['ID1']['APN'])
                if pdp_context_id == 3:
                    subscriber_state_information['ID2']['APN'] = line[49:]
                    print(subscriber_state_information['ID2']['APN'])
                if pdp_context_id == 4:
                    subscriber_state_information['ID3']['APN'] = line[49:]
                    print(subscriber_state_information['ID3']['APN'])
                if pdp_context_id == 5:
                    subscriber_state_information['ID4']['APN'] = line[49:]
                    print(subscriber_state_information['ID4']['APN'])
                continue
        return subscriber_state_information

def xlsx_writter( subscriber_state_information):
    r = str(datetime.now())
    r = r.replace(':','-')#txt_reader/
    file_name_1 = os.path.join('storage' + '/ZMMI_ZMMO_ZMMS_INFO-' + r + '.xlsx')
    # file_name_2 = os.path.join('storage' + '/ZMMS_INFO-' + str(datetime.now()).replace(':', '-') + '.xlsx')

    workbook1 = xlsxwriter.Workbook(file_name_1)
    # workbook2 = xlsxwriter.Workbook(file_name_2)
    worksheet1 = workbook1.add_worksheet()
    # worksheet2 = workbook2.add_worksheet()

    worksheet1.write('A1', 'IMSI')
    worksheet1.write('A2', subscriber_state_information['IMSI'])

    worksheet1.write('B1', 'MSISDN')
    worksheet1.write('B2', subscriber_state_information['MSISDN'])

    worksheet1.write('C1', 'RADIO ACCESS TYPE')
    worksheet1.write('C2', subscriber_state_information['RADIO ACCESS TYPE'])

    worksheet1.write('D1', 'PDP STATE')
    worksheet1.write('D2', subscriber_state_information['PDP STATE'])

    worksheet1.write('E1', 'TERMINAL TYPE')
    worksheet1.write('E2', subscriber_state_information['TERMINAL TYPE'])

    worksheet1.write('F1', 'LAC')
    worksheet1.write('F2', subscriber_state_information['LAC'])

    worksheet1.write('G1', 'CI')
    worksheet1.write('G2', subscriber_state_information['CI'])

    worksheet1.write('I1', 'PDP CONTEXT ID')
    worksheet1.write('I2', subscriber_state_information['ID1']['PDP CONTEXT ID'])
    worksheet1.write('I3', subscriber_state_information['ID2']['PDP CONTEXT ID'])
    worksheet1.write('I4', subscriber_state_information['ID3']['PDP CONTEXT ID'])
    worksheet1.write('I5', subscriber_state_information['ID4']['PDP CONTEXT ID'])

    worksheet1.write('J1', 'QOS PROFILE VERSION')
    worksheet1.write('J2', subscriber_state_information['ID1']['QOS PROFILE VERSION'])
    worksheet1.write('J3', subscriber_state_information['ID2']['QOS PROFILE VERSION'])
    worksheet1.write('J4', subscriber_state_information['ID3']['QOS PROFILE VERSION'])
    worksheet1.write('J5', subscriber_state_information['ID4']['QOS PROFILE VERSION'])

    worksheet1.write('K1', 'APN')
    worksheet1.write('K2', subscriber_state_information['ID1']['APN'])
    worksheet1.write('K3', subscriber_state_information['ID2']['APN'])
    worksheet1.write('K4', subscriber_state_information['ID3']['APN'])
    worksheet1.write('K5', subscriber_state_information['ID4']['APN'])
    workbook1.close()

def main():
    path_to_file = 'storage/test_file.txt'
    path_to_file1 = open(path_to_file, 'r')
    path_to_file1.close()

    path_to_file = os.path.join(path_to_file)
    subscriber_state_information = txt_reader(path_to_file)
    xlsx_writter(subscriber_state_information)
    print(subscriber_state_information)

if __name__ == '__main__':
    main()
