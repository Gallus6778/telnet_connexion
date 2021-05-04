# import zmmi_zmmo_zmms_module
from telnet_sgsn import zmmi_zmmo_zmms_module

import txt_reader as mod

print('Execution complete')
path_to_file = 'storage/test_file.txt'
txt_reader_obj = mod.txt_reader_class(path_to_file)
txt_reader_obj.main()

zmmi_zmmo_zmms_module = zmmi_zmmo_zmms_module.zmmi_zmmo_zmms_class('237669595858')
print(zmmi_zmmo_zmms_module.main())

# txt_reader_obj = txt_reader_class(path_to_file)
# txt_reader_obj.main()