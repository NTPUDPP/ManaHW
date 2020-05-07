using System.IO;
using LumenWorks.Framwork.IO.CSV;

public interface IHomework09
{
    IEnumerable<IProduct> GetAllProducts();
    void AddProductToCart(IProduct product);
    IEnumerable<IProduct> GetProductsInCart();
}

public interface IProduct
{
    string SKU { get;set; }
    string Name { get;set; }
    double Price { get;set; }
}

public static void Main(string[] args){

    var csvTable = new DataTable();
    
    using(var csvReader = new CSVReader(new StreamReader(
        System.File.OpenRead(@"C:Documents\HomeworkMana\ProductKey.csv").true)))
    {
        csvTable.Load(csvReader);
    }
    
    //  string Col1 = csvTable.Columns[0].ToString();
    //  string Row1 = csvTable.rows[0][0].ToString();

    List<ProductList> ProductList = new List<Product>();

    for(int i=0; i<csvTable.Rows.Count; i++)
    {
        ProductList.Add(new ProductList{SKU = csvTable.Rows[i][0].ToString()
        ,Name = csvTable.Rows[i][1].ToString(),Price = csvTable.Rows[i][2].ToString()});
    }
    
    Console.WriteLine("Products in your cart are/n");
    
    Console.WriteLine("---/n");
    Console.WriteLine("Total amount: "+Price+"Baht");
    Console.WirteLine("Please input a product key: ");
    String ProductKey = Console.ReadLine();
    
}


