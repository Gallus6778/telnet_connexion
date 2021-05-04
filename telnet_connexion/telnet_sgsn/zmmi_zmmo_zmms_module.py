#!/usr/bin/python

from datetime import datetime
import asyncio, telnetlib3
import os
import time

class zmmi_zmmo_zmms_class:
    def __init__(self, msisdn):

        self.server_ip = "10.124.206.68"
        self.user = "CHATBO"
        self.password = "1234567890"
        self.MSISDN = msisdn
        self.ZMMI = "ZMMI:MSISDN="
        self.ZMMO = "ZMMO:MSISDN="
        self.ZMMS = "ZMMS:MSISDN="
        self.file_name = os.path.join('telnet_sgsn/storage', self.server_ip+ '-' + str(datetime.now()).replace(':', '-') + '.txt')

        f1 = open(self.file_name, "w")
        f1.close()

    # def msisdn_to_send(msisdn = "237669595858:;"):
    def msisdn_to_send(self, msisdn):
        return msisdn

    @asyncio.coroutine
    def shell(self, reader, writer):
        # MSISDN = msisdn_to_send()
        while True:
            outp = yield from reader.read(65536)
            if not outp:
                # End of File
                break
            elif 'ENTER USERNAME' in outp:
                writer.write(self.user)
                writer.write('\n\r' + self.password + '\n\r' + self.ZMMI + self.MSISDN + ':;\n\r' + self.ZMMO + self.MSISDN + ':;\n\r' + self.ZMMS + self.MSISDN + ':;\n\r')
            # print(outp)
            f1 = open(self.file_name, "a")  # server_ip + "_" + str(datetime.now()) +
            f1.write(outp)
            f1.close()
            time.sleep(2)

        time.sleep(2)

    def main(self):
        loop = asyncio.get_event_loop()
        coro = telnetlib3.open_connection(self.server_ip, 23, shell=self.shell)
        reader, writer = loop.run_until_complete(coro)
        loop.run_until_complete(writer.protocol.waiter_closed)
        file_name = self.file_name
        return file_name

if __name__ == '__main__':
    zmmi_zmmo_zmms = zmmi_zmmo_zmms_class('237669595858')
    zmmi_zmmo_zmms.main()