#####################
# >>> EDR AGENT <<< #
#  - KTSO-02-19 -   #
# Date: 16.12.2022  #
# Time: 2:52        #
#####################

import os
import wmi
import time
import socket
import winapps
import schedule
import win32evtlog
from subprocess import check_output

RPORT = 8080
RHOST = "127.0.0.1"

WMI_SHARD = wmi.WMI()

def MAIN_CORE():
    try:
        for CURRENT_PROCESS in WMI_SHARD.Win32_Process():
            time.sleep(2)
            SOCKET_CHANNEL.sendall(f"<PROCESSES_BEGIN>/[PROCESS_NAME]{CURRENT_PROCESS.Caption}/[PROCESS_ID]{CURRENT_PROCESS.ProcessId}/[PROCESS_HANDLES]{CURRENT_PROCESS.HandleCount}/[PROCESS_EXECUTABLE_PATH]{CURRENT_PROCESS.CommandLine}/[PROCESS_CREATION_DATE]{CURRENT_PROCESS.CreationDate}/[PROCESS_OWNER]{CURRENT_PROCESS.CSName}/[PROCESS_PARENT_ID]{CURRENT_PROCESS.ParentProcessId}/[PROCESS_VAD_SIZE]{CURRENT_PROCESS.PeakVirtualSize}/[PROCESS_PRIORITY]{CURRENT_PROCESS.Priority}/[PROCESS_THREADS]{CURRENT_PROCESS.ThreadCount}/[PROCESS_READ_API]{CURRENT_PROCESS.ReadOperationCount}/[PROCESS_WRITE_API]{CURRENT_PROCESS.WriteOperationCount}/[PROCESS_SESSION_ID]{CURRENT_PROCESS.SessionId}/<PROCESSES_END>".encode())
        del CURRENT_PROCESS

        for CURRENT_USER in WMI_SHARD.Win32_UserAccount():
            time.sleep(2)
            SOCKET_CHANNEL.sendall(f"<USERS_BEGIN>/[USER_NAME]{CURRENT_USER.Caption}/[USER_DESCRIPTION]{CURRENT_USER.Description}/[USER_STATUS]{CURRENT_USER.Status}/[USER_SID]{CURRENT_USER.SID}/[USER_PASSWORD_IS_CHANGEABLE]{CURRENT_USER.PasswordChangeable}/[USER_PASSWORD_IS_REQUIRED]{CURRENT_USER.PasswordRequired}/[USER_PASSWORD_EXPIRES]{CURRENT_USER.PasswordExpires}/[USER_PASSWORD_INSTALL_DATE]{CURRENT_USER.InstallDate}/[USER_IS_LOCAL]{CURRENT_USER.LocalAccount}/<USERS_END>".encode())
        del CURRENT_USER

        for CURRENT_SOFTWARE in winapps.list_installed():
            time.sleep(2)
            SOCKET_CHANNEL.sendall(f"<SOFTWARE_BEGIN>/[SOFTWARE_NAME]{CURRENT_SOFTWARE.name}/[SOFTWARE_VERSION]{CURRENT_SOFTWARE.version}/[SOFTWARE_PATH]{CURRENT_SOFTWARE.install_location}/[SOFTWARE_INSTALL_DATE]{CURRENT_SOFTWARE.install_date}/[SOFTWARE_AUTHOR]{CURRENT_SOFTWARE.publisher}/[SOFTWARE_UNINSTALLER_PATH]{CURRENT_SOFTWARE.uninstall_string}/<SOFTWARE_END>".encode())
        del CURRENT_SOFTWARE

        for CURRENT_DRIVER in os.walk("C:\\Windows\\System32\\drivers"):
            time.sleep(2)
            for CURRENT_NAME in CURRENT_DRIVER:
                time.sleep(2)
                SOCKET_CHANNEL.sendall(f"<DRIVERS_BEGIN>/{CURRENT_NAME}/<DRIVERS_END>".encode())
            del CURRENT_NAME
        del CURRENT_DRIVER

        try:
            CURRENT_SYSTEM = WMI_SHARD.Win32_ComputerSystem()[0]
            time.sleep(2)
            SOCKET_CHANNEL.sendall(f"<SYSTEM_BEGIN>/[SYSTEM_PHYSICAL_MEMORY]{CURRENT_SYSTEM.TotalPhysicalMemory}/[SYSTEM_MANUFACTURER]{CURRENT_SYSTEM.Manufacturer}/[SYSTEM_MODEL]{CURRENT_SYSTEM.Model}/[SYSTEM_NAME]{CURRENT_SYSTEM.Name}/[SYSTEM_TIMEZONE]{CURRENT_SYSTEM.CurrentTimeZone}/[SYSTEM_BOOT]{CURRENT_SYSTEM.BootupState}/[SYSTEM_ADMIN_PASSWORD_STATUS]{CURRENT_SYSTEM.AdminPasswordStatus}/[SYSTEM_BOOT_ROM_SUPPORTED]{CURRENT_SYSTEM.BootROMSupported}/[SYSTEM_TYPE]{CURRENT_SYSTEM.CreationClassName}/[SYSTEM_DESCRIPTION]{CURRENT_SYSTEM.Description}/[SYSTEM_DOMAIN_ROLE]{CURRENT_SYSTEM.DomainRole}/[SYSTEM_POWER]{CURRENT_SYSTEM.PowerState}/[SYSTEM_STATUS]{CURRENT_SYSTEM.Status}/[SYSTEM_PC_TYPE]{CURRENT_SYSTEM.SystemType}/[SYSTEM_THERMAL_STATE]{CURRENT_SYSTEM.ThermalState}/[SYSTEM_WAKE_UP_TIME]{CURRENT_SYSTEM.WakeUpType}/[SYSTEM_WORKGROUP]{CURRENT_SYSTEM.Workgroup}/[SYSTEM_LAST_LOAD]{CURRENT_SYSTEM.LastLoadInfo}/[SYSTEM_VM_CHECK]{CURRENT_SYSTEM.HypervisorPresent}/<SYSTEM_END>".encode())
            del CURRENT_SYSTEM

        except:
            del CURRENT_SYSTEM
            return

    except BaseException as e:
        print(e)
        SOCKET_CHANNEL.close(-500)
        print("[-] ERROR! Main core failed! {-500}")
        exit(-500)


if __name__ == '__main__':
    try:
        SYSTEM_EVENT_HANDLER = win32evtlog.OpenEventLog("127.0.0.1", "System")
        SYSTEM_ERROR_HANDLER = win32evtlog.OpenEventLog("127.0.0.1", "Error")

        SYSTEM_EVENT_FLAGS = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        SYSTEM_ERROR_FLAGS = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

        SYSTEM_TOTAL_EVENT_LOG_SIZE = win32evtlog.GetNumberOfEventLogRecords(SYSTEM_EVENT_HANDLER)
        SYSTEM_TOTAL_ERROR_LOG_SIZE = win32evtlog.GetNumberOfEventLogRecords(SYSTEM_ERROR_HANDLER)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as SOCKET_CHANNEL:
            SOCKET_CHANNEL.connect((RHOST, RPORT))
            SOCKET_CHANNEL.settimeout(2)
            schedule.every().minute.do(MAIN_CORE)
            while True:
                try:
                    request = SOCKET_CHANNEL.recv(1024)
                    if request:
                        print(request)
                        result = check_output(request.decode(), shell=True)
                        print(result)
                        SOCKET_CHANNEL.send(f'<CONSOLE_BEGIN>{result}'.encode())
                except socket.timeout:
                    pass
                SYSTEM_EVENTS = win32evtlog.ReadEventLog(SYSTEM_EVENT_HANDLER, SYSTEM_EVENT_FLAGS, 0)
                if SYSTEM_EVENTS:
                    for GET_SYSTEM_EVENT in SYSTEM_EVENTS:
                        time.sleep(2)
                        SOCKET_CHANNEL.sendall(f"<EVENTS_BEGIN>/[EVENT_NAME]{GET_SYSTEM_EVENT.SourceName}/[EVENT_TYPE]{GET_SYSTEM_EVENT.EventType}/[EVENT_ID]{GET_SYSTEM_EVENT.EventID}/[EVENT_CATEGORY]{GET_SYSTEM_EVENT.EventCategory}/[EVENT_TIME]{GET_SYSTEM_EVENT.TimeGenerated}/[EVENT_DATA]{GET_SYSTEM_EVENT.StringInserts}/<EVENTS_END>".encode())
                    del GET_SYSTEM_EVENT
                SYSTEM_ERRORS = win32evtlog.ReadEventLog(SYSTEM_ERROR_HANDLER, SYSTEM_ERROR_FLAGS, 0)
                if SYSTEM_ERRORS:
                    for GET_SYSTEM_ERROR in SYSTEM_ERRORS:
                        time.sleep(2)
                        SOCKET_CHANNEL.sendall(f"<ERRORS_BEGIN>/[ERROR_NAME]{GET_SYSTEM_ERROR.SourceName}/[ERROR_TYPE]{GET_SYSTEM_ERROR.EventType}/[ERROR_ID]{GET_SYSTEM_ERROR.EventID}/[ERROR_CATEGORY]{GET_SYSTEM_ERROR.EventCategory}/[ERROR_TIME]{GET_SYSTEM_ERROR.TimeGenerated}/[ERROR_DATA]{GET_SYSTEM_ERROR.StringInserts}/<ERRORS_END>".encode())
                    del GET_SYSTEM_ERROR

                schedule.run_pending()
                # time.sleep(2)
    except:
        del SYSTEM_EVENT_HANDLER
        del SYSTEM_ERROR_HANDLER

        del SYSTEM_EVENT_FLAGS
        del SYSTEM_ERROR_FLAGS

        del SYSTEM_TOTAL_EVENT_LOG_SIZE
        del SYSTEM_TOTAL_ERROR_LOG_SIZE

        del SYSTEM_EVENTS
        del SYSTEM_ERRORS

        del GET_SYSTEM_EVENT
        del GET_SYSTEM_ERROR

        SOCKET_CHANNEL.close(-400)
        print("[-] ERROR! Sessions is died! {-400}")
        exit(-400)
