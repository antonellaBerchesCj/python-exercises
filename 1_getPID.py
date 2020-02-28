'''
1. [ctypes] Get the process name from a process ID (CreateToolhelp32Snapshot, TH32CS_SNAPPROCESS, szExeFile).
'''

from ctypes import c_long , c_int , c_uint , c_char , c_ubyte , c_char_p , c_void_p
from ctypes import windll
from ctypes import Structure
from ctypes import sizeof , POINTER , pointer , cast

TH32CS_SNAPPROCESS = 2
STANDARD_RIGHTS_REQUIRED = 0x000F0000
SYNCHRONIZE = 0x00100000
PROCESS_ALL_ACCESS = (STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0xFFF)

class PROCESSENTRY32(Structure):
    _fields_ = [ ( 'dwSize' , c_uint ) , 
                 ( 'cntUsage' , c_uint) ,
                 ( 'th32ProcessID' , c_uint) ,
                 ( 'th32DefaultHeapID' , c_uint) ,
                 ( 'th32ModuleID' , c_uint) ,
                 ( 'cntThreads' , c_uint) ,
                 ( 'th32ParentProcessID' , c_uint) ,
                 ( 'pcPriClassBase' , c_long) ,
                 ( 'dwFlags' , c_uint) ,
                 ( 'szExeFile' , c_char * 260 ) , 
                 ( 'th32MemoryBase' , c_long) ,
                 ( 'th32AccessKey' , c_long ) ]

# forigen function
CreateToolhelp32Snapshot= windll.kernel32.CreateToolhelp32Snapshot
CreateToolhelp32Snapshot.reltype = c_long
CreateToolhelp32Snapshot.argtypes = [ c_int , c_int ]

Process32First = windll.kernel32.Process32First
Process32First.argtypes = [ c_void_p , POINTER( PROCESSENTRY32 ) ]
Process32First.rettype = c_int

Process32Next = windll.kernel32.Process32Next
Process32Next.argtypes = [ c_void_p , POINTER(PROCESSENTRY32) ]
Process32Next.rettype = c_int

OpenProcess = windll.kernel32.OpenProcess
OpenProcess.argtypes = [ c_void_p , c_int , c_long ]
OpenProcess.rettype = c_long

GetPriorityClass = windll.kernel32.GetPriorityClass
GetPriorityClass.argtypes = [ c_void_p ]
GetPriorityClass.rettype = c_long

CloseHandle = windll.kernel32.CloseHandle
CloseHandle.argtypes = [ c_void_p ]
CloseHandle.rettype = c_int

GetLastError = windll.kernel32.GetLastError
GetLastError.rettype = c_long

if __name__ == '__main__' :
    hProcessSnap = c_void_p(0)
    hProcessSnap = CreateToolhelp32Snapshot( TH32CS_SNAPPROCESS , 0 )

    pe32 = PROCESSENTRY32()
    pe32.dwSize = sizeof( PROCESSENTRY32 )
    ret = Process32First( hProcessSnap , pointer( pe32 ) )

    while ret :
        print ("Process Name : %s " % pe32.szExeFile)

        hProcess = OpenProcess( PROCESS_ALL_ACCESS , 0 , pe32.th32ProcessID )
        dwPriorityClass = GetPriorityClass( hProcess )
        if dwPriorityClass == 0 :
            CloseHandle( hProcess )

        print("  PID = 0x%08X" % pe32.th32ProcessID)
        ret = Process32Next( hProcessSnap, pointer(pe32) )
