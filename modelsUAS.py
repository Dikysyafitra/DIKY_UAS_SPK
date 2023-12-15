from sqlalchemy import String, Integer
from sqlalchemy.orm import declarative_base, Mapped, mapped_column


class Base(declarative_base):
    pass


class leptop(Base): 
    __tablename__ = "tbl_laptop"
    no = Mapped[Integer] = mapped_column(primary_key=True)
    brand = Mapped[String] = mapped_column()
    ram = Mapped[String] = mapped_column()
    cpu = Mapped[String] = mapped_column()
    gpu = Mapped[String] = mapped_column()
    baterai = Mapped[String] = mapped_column()
    harga = Mapped[String] = mapped_column()
    ukuran_layar = Mapped[String] = mapped_column()

    def _repr_(self):
        return f"leptop(brand={self.brand!r}, ram={self.ram!r}, cpu={self.cpu!r}, gpu={self.gpu!r}, baterai={self.baterai!r}, harga={self.harga!r}, ukuran_layar={self.ukuran_layar!r})"