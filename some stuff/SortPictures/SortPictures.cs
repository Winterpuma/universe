using System;
using System.IO;

namespace ConsoleApp2
{
    class Program
    {
        /// <summary>
        /// Will get files from sourse and move them to dest\\YYYY\\MMDD, where
        /// YYYYMMDD is part of filename.
        /// </summary>
        /// <param name="sourse"></param>
        /// <param name="dest"></param>
        /// <param name="spaceBeforeDate">"Img_20190903" space is 4</param>
        static void MovePics(DirectoryInfo sourse, DirectoryInfo dest, int spaceBeforeDate = 0)
        {
            foreach (FileInfo file in sourse.GetFiles())
            {
                string year = file.Name.Substring(spaceBeforeDate, 4);
                string date = file.Name.Substring(spaceBeforeDate + 4, 4);

                string resDerictory = dest + "\\" + year + "\\" + date;
                Directory.CreateDirectory(resDerictory);
                file.CopyTo(resDerictory + "\\" + file.Name.Substring(spaceBeforeDate)); // will delete all chars before date in filename
            }
        }

        static void Main(string[] args)
        {
            DirectoryInfo sourse = new DirectoryInfo(@"D:\test");
            DirectoryInfo dest = new DirectoryInfo(@"D:\test");

            MovePics(sourse, dest, 0);
        }
    }
}
