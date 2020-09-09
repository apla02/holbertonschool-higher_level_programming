#include <stdio.h>
#include <stdlib.h>
#include "/usr/local/include/python3.4m/Python.h"
void print_python_list_info(PyObject *p)
{
	int i = 0;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject*)(p))->allocated);
	for(i = 0; i < PyList_Size(p); i++)
		printf("Element %i: %s\n", i, (Py_TYPE(PyList_GetItem(p, i))->tp_name));
}
