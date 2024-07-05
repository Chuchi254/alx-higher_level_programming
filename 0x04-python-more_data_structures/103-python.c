#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - Prints basic info about Python bytes object
 * @p: A PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf(" size: %zd\n", size);
	printf(" trying string: %s\n", str);
	printf(" first %zd bytes: ", size < 10 ? size + 1 : 10);

	for (i = 0; i < size + 1 && i < 10; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i < 9)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_list - Prints basic info about Python lists
 * @p: A PyObject list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %zd: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
	}
}
