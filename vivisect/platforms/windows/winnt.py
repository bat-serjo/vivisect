import vivisect.hal.memory as v_memory

INFINITE = 0xffffffff
EXCEPTION_MAXIMUM_PARAMETERS = 15

# Debug Event Types
EXCEPTION_DEBUG_EVENT       =1
CREATE_THREAD_DEBUG_EVENT   =2
CREATE_PROCESS_DEBUG_EVENT  =3
EXIT_THREAD_DEBUG_EVENT     =4
EXIT_PROCESS_DEBUG_EVENT    =5
LOAD_DLL_DEBUG_EVENT        =6
UNLOAD_DLL_DEBUG_EVENT      =7
OUTPUT_DEBUG_STRING_EVENT   =8
RIP_EVENT                   =9

# Symbol Flags
SYMFLAG_VALUEPRESENT     = 0x00000001
SYMFLAG_REGISTER         = 0x00000008
SYMFLAG_REGREL           = 0x00000010
SYMFLAG_FRAMEREL         = 0x00000020
SYMFLAG_PARAMETER        = 0x00000040
SYMFLAG_LOCAL            = 0x00000080
SYMFLAG_CONSTANT         = 0x00000100
SYMFLAG_EXPORT           = 0x00000200
SYMFLAG_FORWARDER        = 0x00000400
SYMFLAG_FUNCTION         = 0x00000800
SYMFLAG_VIRTUAL          = 0x00001000
SYMFLAG_THUNK            = 0x00002000
SYMFLAG_TLSREL           = 0x00004000

# Symbol Resolution Options
SYMOPT_CASE_INSENSITIVE         = 0x00000001
SYMOPT_UNDNAME                  = 0x00000002
SYMOPT_DEFERRED_LOADS           = 0x00000004
SYMOPT_NO_CPP                   = 0x00000008
SYMOPT_LOAD_LINES               = 0x00000010
SYMOPT_OMAP_FIND_NEAREST        = 0x00000020
SYMOPT_LOAD_ANYTHING            = 0x00000040
SYMOPT_IGNORE_CVREC             = 0x00000080
SYMOPT_NO_UNQUALIFIED_LOADS     = 0x00000100
SYMOPT_FAIL_CRITICAL_ERRORS     = 0x00000200
SYMOPT_EXACT_SYMBOLS            = 0x00000400
SYMOPT_ALLOW_ABSOLUTE_SYMBOLS   = 0x00000800
SYMOPT_IGNORE_NT_SYMPATH        = 0x00001000
SYMOPT_INCLUDE_32BIT_MODULES    = 0x00002000
SYMOPT_PUBLICS_ONLY             = 0x00004000
SYMOPT_NO_PUBLICS               = 0x00008000
SYMOPT_AUTO_PUBLICS             = 0x00010000
SYMOPT_NO_IMAGE_SEARCH          = 0x00020000
SYMOPT_SECURE                   = 0x00040000
SYMOPT_NO_PROMPTS               = 0x00080000
SYMOPT_OVERWRITE                = 0x00100000
SYMOPT_DEBUG                    = 0x80000000

# Exception Types
EXCEPTION_WAIT_0                  = 0x00000000
EXCEPTION_ABANDONED_WAIT_0        = 0x00000080
EXCEPTION_USER_APC                = 0x000000c0
EXCEPTION_TIMEOUT                 = 0x00000102
EXCEPTION_PENDING                 = 0x00000103
DBG_EXCEPTION_HANDLED             = 0x00010001
DBG_CONTINUE                      = 0x00010002
EXCEPTION_SEGMENT_NOTIFICATION    = 0x40000005
DBG_TERMINATE_THREAD              = 0x40010003
DBG_TERMINATE_PROCESS             = 0x40010004
DBG_CONTROL_C                     = 0x40010005
DBG_CONTROL_BREAK                 = 0x40010008
DBG_COMMAND_EXCEPTION             = 0x40010009
EXCEPTION_GUARD_PAGE_VIOLATION       = 0x80000001
EXCEPTION_DATATYPE_MISALIGNMENT      = 0x80000002
EXCEPTION_BREAKPOINT                 = 0x80000003
STATUS_WX86_BREAKPOINT               = 0x4000001f
EXCEPTION_SINGLE_STEP                = 0x80000004
STATUS_WX86_SINGLE_STEP              = 0x4000001e
DBG_EXCEPTION_NOT_HANDLED            = 0x80010001
STATUS_BUFFER_OVERFLOW               = 0x80000005
STATUS_SUCCESS                       = 0x00000000
STATUS_INFO_LENGTH_MISMATCH          = 0xc0000004
EXCEPTION_ACCESS_VIOLATION           = 0xc0000005
EXCEPTION_IN_PAGE_ERROR              = 0xc0000006
EXCEPTION_INVALID_HANDLE             = 0xc0000008
EXCEPTION_NO_MEMORY                  = 0xc0000017
EXCEPTION_ILLEGAL_INSTRUCTION        = 0xc000001d
EXCEPTION_NONCONTINUABLE_EXCEPTION   = 0xc0000025
EXCEPTION_INVALID_DISPOSITION        = 0xc0000026
EXCEPTION_ARRAY_BOUNDS_EXCEEDED      = 0xc000008c
EXCEPTION_FLOAT_DENORMAL_OPERAND     = 0xc000008D
EXCEPTION_FLOAT_DIVIDE_BY_ZERO       = 0xc000008e
EXCEPTION_FLOAT_INEXACT_RESULT       = 0xc000008f
EXCEPTION_FLOAT_INVALID_OPERATION    = 0xc0000090
EXCEPTION_FLOAT_OVERFLOW             = 0xc0000091
EXCEPTION_FLOAT_STACK_CHECK          = 0xc0000092
EXCEPTION_FLOAT_UNDERFLOW            = 0xc0000093
EXCEPTION_INTEGER_DIVIDE_BY_ZERO     = 0xc0000094
EXCEPTION_INTEGER_OVERFLOW           = 0xc0000095
EXCEPTION_PRIVILEGED_INSTRUCTION     = 0xc0000096
EXCEPTION_STACK_OVERFLOW             = 0xc00000fd
EXCEPTION_CONTROL_C_EXIT             = 0xc000013a
EXCEPTION_FLOAT_MULTIPLE_FAULTS      = 0xc00002b4
EXCEPTION_FLOAT_MULTIPLE_TRAPS       = 0xc00002b5
EXCEPTION_REG_NAT_CONSUMPTION        = 0xc00002c9

# Context Info
CONTEXT_i386    = 0x00010000    # this assumes that i386 and
CONTEXT_i486    = 0x00010000    # i486 have identical context records
CONTEXT_AMD64   = 0x00100000    # For amd x64...

CONTEXT_CONTROL         = 0x00000001 # SS:SP, CS:IP, FLAGS, BP
CONTEXT_INTEGER         = 0x00000002 # AX, BX, CX, DX, SI, DI
CONTEXT_SEGMENTS        = 0x00000004 # DS, ES, FS, GS
CONTEXT_FLOATING_POINT  = 0x00000008 # 387 state
CONTEXT_DEBUG_REGISTERS = 0x00000010 # DB 0-3,6,7
CONTEXT_EXTENDED_REGISTERS  = 0x00000020 # cpu specific extensions
CONTEXT_FULL = (CONTEXT_CONTROL | CONTEXT_INTEGER | CONTEXT_SEGMENTS)
CONTEXT_ALL = (CONTEXT_CONTROL | CONTEXT_INTEGER | CONTEXT_SEGMENTS | CONTEXT_FLOATING_POINT | CONTEXT_DEBUG_REGISTERS | CONTEXT_EXTENDED_REGISTERS)


# Thread Permissions
THREAD_ALL_ACCESS   = 0x001f03ff
PROCESS_ALL_ACCESS  = 0x001f0fff

# NtQueryInformationProcess classes
ProcessBasicInformation     = 0
ProcessDebugPort            = 7
ProcessWow64Information     = 26
ProcessImageFileName        = 27
ProcessBreakOnTermination   = 29

# Memory Permissions
PAGE_NOACCESS           = 0x01
PAGE_READONLY           = 0x02
PAGE_READWRITE          = 0x04
PAGE_WRITECOPY          = 0x08
PAGE_EXECUTE            = 0x10
PAGE_EXECUTE_READ       = 0x20
PAGE_EXECUTE_READWRITE  = 0x40
PAGE_EXECUTE_WRITECOPY  = 0x80
PAGE_GUARD              = 0x100
PAGE_NOCACHE            = 0x200
PAGE_WRITECOMBINE       = 0x400

perm_lookup = {
    PAGE_NOACCESS:0,
    PAGE_READONLY:v_memory.MM_READ,
    PAGE_READWRITE: v_memory.MM_READ | v_memory.MM_WRITE,
    PAGE_WRITECOPY: v_memory.MM_READ | v_memory.MM_WRITE,
    PAGE_EXECUTE: v_memory.MM_EXEC,
    PAGE_EXECUTE_READ: v_memory.MM_EXEC | v_memory.MM_READ,
    PAGE_EXECUTE_READWRITE: v_memory.MM_EXEC | v_memory.MM_READ | v_memory.MM_WRITE,
    PAGE_EXECUTE_WRITECOPY: v_memory.MM_EXEC | v_memory.MM_READ | v_memory.MM_WRITE,
}

SE_PRIVILEGE_ENABLED    = 0x00000002
TOKEN_ADJUST_PRIVILEGES = 0x00000020
TOKEN_QUERY             = 0x00000008
dbgprivdone = False

# TOKEN_INFORMATION_CLASS
TokenUser                   = 1
TokenGroups                 = 2
TokenPrivileges             = 3
TokenOwner                  = 4
TokenPrimaryGroup           = 5
TokenDefaultDacl            = 6
TokenSource                 = 7
TokenType                   = 8
TokenImpersonationLevel     = 9
TokenStatistics             = 10
TokenRestrictedSids         = 11
TokenSessionId              = 12
TokenGroupsAndPrivileges    = 13
TokenSessionReference       = 14
TokenSandBoxInert           = 15
TokenAuditPolicy            = 16
TokenOrigin                 = 17
TokenElevationType          = 18
TokenLinkedToken            = 19
TokenElevation              = 20
TokenHasRestrictions        = 21
TokenAccessInformation      = 22
TokenVirtualizationAllowed  = 23
TokenVirtualizationEnabled  = 24
TokenIntegrityLevel         = 25
TokenUIAccess               = 26
TokenMandatoryPolicy        = 27
TokenLogonSid               = 28
MaxTokenInfoClass           = 29

# TOKEN_ELEVATION_TYPE
TokenElevationTypeDefault   = 1
TokenElevationTypeFull      = 2
TokenElevationTypeLimited   = 3

# FIXME maybe this goes in plats?
PROCESSOR_ARCHITECTURE_INTEL            = 0
PROCESSOR_ARCHITECTURE_MIPS             = 1
PROCESSOR_ARCHITECTURE_ALPHA            = 2
PROCESSOR_ARCHITECTURE_PPC              = 3
PROCESSOR_ARCHITECTURE_SHX              = 4
PROCESSOR_ARCHITECTURE_ARM              = 5
PROCESSOR_ARCHITECTURE_IA64             = 6
PROCESSOR_ARCHITECTURE_ALPHA64          = 7
PROCESSOR_ARCHITECTURE_MSIL             = 8
PROCESSOR_ARCHITECTURE_AMD64            = 9
PROCESSOR_ARCHITECTURE_IA32_ON_WIN64    = 10
PROCESSOR_ARCHITECTURE_UNKNOWN          = 0xFFFF

# Memory States
MEM_COMMIT = 0x1000
MEM_FREE = 0x10000
MEM_RESERVE = 0x2000

# Memory Types
MEM_IMAGE = 0x1000000
MEM_MAPPED = 0x40000
MEM_PRIVATE = 0x20000

# Process Creation Flags
DEBUG_ONLY_THIS_PROCESS     = 0x02

