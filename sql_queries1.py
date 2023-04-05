CREATE_DW =  '''

CREATE TABLE sales_territory (
    TerritoryID INT,
    Name_ VARCHAR(14),
    CountryRegionCode CHAR(3),
    Group_ VARCHAR(14),
    SalesYTD INT,
    SalesLastYear INT,
    CostYTD INT,
    CostLastYear INT,
    rowguid CHAR(36),
    ModifiedDate DATETIME,
    INDEX (TerritoryID),
    PRIMARY KEY (TerritoryID)
) ;

CREATE TABLE sales_costumer (
    CustomerID INT PRIMARY KEY,
    PersonID INT,
    StoreID INT,
    TerritoryID INT,
    AccountNumber CHAR(10),
    rowguid CHAR(36),
    ModifiedDate DATETIME
) ;


CREATE TABLE production_product (
    ProductID INT PRIMARY KEY,
    Name_ VARCHAR(50),
    ProductNumber VARCHAR(10),
    MakeFlag INT,
    FinishedGoodsFlag INT,
    Color VARCHAR(15),
    SafetyStockLevel INT,
    ReorderPoint INT,
    StandardCost DECIMAL(10 , 4 ),
    ListPrice DECIMAL(10 , 2 ),
    Size VARCHAR(4),
    SizeUnitMeasureCode VARCHAR(4),
    WeightUnitMeasureCode VARCHAR(4),
    Weight DECIMAL(10 , 2 ),
    DaysToManufacture INT,
    ProductLine VARCHAR(4),
    Class VARCHAR(4),
    Style VARCHAR(4),
    ProductSubcategoryID INT,
    ProductModelID INT,
    SellStartDate DATETIME,
    SellEndDate DATETIME,
    DiscontinuedDate DATETIME,
    rowguid VARCHAR(36),
    ModifiedDate DATETIME
)  ENGINE=INNODB;


CREATE TABLE fact_sales_order_header (
    SalesOrderID INT PRIMARY KEY,
    RevisionNumber INT,
    OrderDate DATETIME,
    DueDate DATETIME,
    ShipDate DATETIME,
    Status_ INT,
    OnlineOrderFlag INT,
    SalesOrderNumber CHAR(7),
    PurchaseOrderNumber VARCHAR(13),
    AccountNumber CHAR(14),
    CustomerID INT,
    SalesPersonID INT,
    TerritoryID INT,
    BillToAddressID INT,
    ShipToAddressID INT,
    ShipMethodID INT,
    CreditCardID INT,
    CreditCardApprovalCode VARCHAR(15),
    CurrencyRateID INT,
    SubTotal DECIMAL(10 , 4 ),
    TaxAmt DECIMAL(10 , 4 ),
    Freight DECIMAL(10 , 4 ),
    TotalDue DECIMAL(10 , 4 ),
    Comment_ VARCHAR(5),
    ModifiedDate DATETIME,
    CONSTRAINT ck_territoryid FOREIGN KEY (TerritoryID)
        REFERENCES sales_territory (TerritoryID),
    CONSTRAINT ck_customerid FOREIGN KEY (CustomerID)
        REFERENCES sales_costumer (CustomerID)
);


-- Tabla Sales.SalesOrderDetail

CREATE TABLE sales_order_detail (
    SalesOrderDetailID INT PRIMARY KEY,
    SalesOrderID INT,
    CarrierTrackingNumber VARCHAR(12),
    OrderQty INT,
    ProductID INT,
    SpecialOfferID INT,
    UnitPrice DECIMAL(10 , 4 ),
    UnitPriceDiscount DECIMAL(10 , 4 ),
    LineTotal DECIMAL(10 , 4 ),
    rowguid CHAR(36),
    ModifiedDate DATETIME,
    INDEX (SalesOrderID),
    CONSTRAINT ck_productid FOREIGN KEY (ProductID)
        REFERENCES production_product (ProductID),
    CONSTRAINT ck_sale FOREIGN KEY (SalesOrderID)
        REFERENCES fact_sales_order_header (SalesOrderID)
); '''