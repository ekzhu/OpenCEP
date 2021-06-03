from OpenCEP import Pattern, SeqOperator, PrimitiveEventStructure, SimpleCondition, Variable, timedelta, FileInputStream, FileOutputStream
from OpenCEP.plugin.stocks.Stocks import MetastockDataFormatter
from OpenCEP import CEP

googleAscendPattern = Pattern(
    SeqOperator(PrimitiveEventStructure("GOOG", "a"),
                PrimitiveEventStructure("GOOG", "b"),
                PrimitiveEventStructure("GOOG", "c")),
    SimpleCondition(Variable("a", lambda x: x["Peak Price"]),
                    Variable("b", lambda x: x["Peak Price"]),
                    Variable("c", lambda x: x["Peak Price"]),
                    relation_op=lambda x, y, z: x < y < z),
    timedelta(minutes=3)
)

cep = CEP([googleAscendPattern])

events = FileInputStream("test/EventFiles/NASDAQ_SHORT.txt")

cep.run(events,
        FileOutputStream(
            ".",
            'output.txt'), MetastockDataFormatter())
