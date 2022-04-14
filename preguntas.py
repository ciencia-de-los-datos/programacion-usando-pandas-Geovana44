"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
from operator import index
import pandas as pd 

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    filas = len(tbl0)
    return filas


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    col = tbl0.shape[1]
    return col



def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    name_col1 = tbl0.columns[1]
    
    col1 = tbl0[name_col1].value_counts() #col1 = tbl0.iloc[:,[1]]
    total = col1.sort_index()
    return total


def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    name_col1 = tbl0.columns[1]
    name_col2 = tbl0.columns[2]
    total =tbl0.groupby(name_col1)[name_col2].mean()
    return total


def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    name_col1 = tbl0.columns[1]
    name_col2 = tbl0.columns[2]
    total =tbl0.groupby(name_col1)[name_col2].max()
    return total
    


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    tblf = tbl1.drop_duplicates("_c4").values
    col4 = [i[1].upper() for i in tblf]
    return sorted(col4)


def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    name_col1 = tbl0.columns[1]
    name_col2 = tbl0.columns[2]
    total =tbl0.groupby(name_col1)[name_col2].sum()
    return total


def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    suma={"suma":tbl0["_c0"]+tbl0["_c2"]}
    sumaf= pd.DataFrame(data=suma)
    total = pd.concat([tbl0,sumaf], axis=1)
    return total


def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
   
    col3 =[ i.split("-") for i in tbl0["_c3"].values]   
    year=pd.DataFrame(data={"year":[i[0] for i in col3]})
    total = pd.concat([tbl0,year], axis=1)
    return total


def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    
    
    """
    letter= sorted(tbl0["_c1"].unique())
    valores =tbl0.groupby("_c1")["_c2"] 
    listafin= [":".join(map(str, valores.get_group(i))) for i in letter]
    d1=pd.DataFrame({"_c0":letter})
    d2=pd.DataFrame({"_c1":listafin})
    total = pd.concat([d1,d2], axis=1)
    total.set_index("_c0", inplace=True)
    #valores =list(tbl0.groupby("_c1", as_index=False)["_c2"].__iter__())
    #total = pd.concat(,total], axis=1)
    return total


def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    num= sorted(tbl1["_c0"].unique())
    valores =tbl1.groupby("_c0")["_c4"] 
    listafin= [",".join(map(str, sorted(valores.get_group(i)))) for i in num]
    d1=pd.DataFrame({"_c0":num})
    d2=pd.DataFrame({"_c4":listafin})
    total = pd.concat([d1,d2], axis=1)
    return total


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    se estan juntando dos columans y la separamos por :
    sorted(valores.get_group(i)["_c5a"].map(str)+ ":"+ valores.get_group(i)["_c5b"].map(str))
    """
    
    valores = tbl2.groupby("_c0")[["_c5a","_c5b"]]
    num= sorted(tbl2["_c0"].unique())
    b=[",".join(map(str, sorted(valores.get_group(i)["_c5a"].map(str)+ ":"+ valores.get_group(i)["_c5b"].map(str)))) for i in num]
    d1=pd.DataFrame({"_c0":num})
    d2=pd.DataFrame({"_c5":b})
    total = pd.concat([d1,d2], axis=1)
    
    return total


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    nueva= pd.merge(tbl0,tbl2, on="_c0")  #combina tabla segun _Co para dejarla de la dim mayor
    valores = nueva.groupby("_c1")["_c5b"].sum()
    

    return valores

    
"""
        Otro 10 no sirvio
        datar = tbl0.drop_duplicates("_c1")
        letter=datar["_c1"].values
        letter.sort()
        valores =tbl0.groupby("_c1")["_c2"]
        listafin= [valores.get_group(i).values for i in letter]
        listafin = [str(sorted(listafin[i])).replace(",",":").replace("[","").replace("]","") for i in range(len(listafin))]
        total = pd.concat([pd.DataFrame(data={"_c0":letter}),pd.DataFrame(data={"_c1":listafin})], axis=1)
        
        letter= sorted(tbl0["_c1"].unique())
        valores =tbl0.groupby("_c1")["_c2"] 
        listafin= [":".join(map(str, valores.get_group(i))) for i in letter]
        d1=pd.DataFrame({"_c0":letter})
        d2=pd.DataFrame({"_c1":listafin})
        total = pd.concat([d1,d2], axis=1)
        total.set_index("_c0", inplace=True)
"""
