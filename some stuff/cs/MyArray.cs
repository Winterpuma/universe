using System;
using System.Collections.Generic;

namespace ConsoleApp3
{
    class MyArray
    {
        int[] array;

        public MyArray(int n)
        {
            array = new int[n];
        }

        public void FillManual()
        {
            for (int i = 0; i < array.Length; i++)
            {
                array[i] = Convert.ToInt32(Console.ReadLine());
            }
        }

        public void FillRandom()
        {
            var rand = new Random();
            for (int i = 0; i < array.Length; i++)
            {
                array[i] = rand.Next(100);
            }
        }

        public void Output()
        {
            for (int i = 0; i < array.Length; i++)
            {
                Console.Write(array[i] + ' ');
            }
            Console.WriteLine();
        }
        
        public void SortEvenPositions()
        {
            if (array.Length <= 3)
                return;
            List<int> m;
            
            int temp;
            bool swapped = true;

            while (swapped)
            {
                swapped = false;
                for (int i = 2; i < array.Length; i += 2)
                {
                    if (array[i] > array[i - 2])
                    {
                        swapped = true;
                        temp = array[i];
                        array[i] = array[i - 2];
                        array[i - 2] = temp;
                    }
                }
            }
        }
    }
}
