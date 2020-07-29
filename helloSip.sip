// Define the SIP wrapper to the (actual) helloSip library.

%Module(name=helloSip, language="C++")

%ModuleCode
#include <helloSip.h>
%End

void helloFromCpp();