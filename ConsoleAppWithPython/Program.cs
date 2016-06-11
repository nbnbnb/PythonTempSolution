using IronPython.Hosting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleAppWithPython
{
    class Program
    {
        static void Main(string[] args)
        {
            // 安装 Python 库

            //Install - Package IronPython
            //Install - Package IronPython.StdLib

            var engine = Python.CreateEngine();
            engine.CreateScriptSourceFromString("print('Hello IronPython!')").Execute();
        }
    }
}
