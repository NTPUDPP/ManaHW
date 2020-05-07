   
using System;

interface LightBulb
{
    void checkLight(string[] open,string[] check);
}


class Light : LightBulb
{
    public void checkLight(string[] led_open,string[] light_stat)
    {
                string lednum = Console.ReadLine();
                for (int i = 0; i < 10; i++)
                {
                    if (led_open[i] == lednum & light_stat[i] == "[]")
                    {
                        light_stat[i] = "[!]";
                    }
                    else if (led_open[i] == lednum & light_stat[i] == "[!]")
                    {
                        light_stat[i] = "[]";
                    }
                    
                }
                 Console.WriteLine(string.Join(" ", check)); //Stack 
    }
}

class Program
{   
    static void Main(string[] args)
    {
        Light Light = new Light();
        string[] led_open = { "1", "2", "3", "4", "5", "6", "7", "8", "9", "A" };
        string[] light_stat = { "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]"};
        Light.checkLight(led_open,light_stat);
    }
}