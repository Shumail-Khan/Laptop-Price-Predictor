from pydantic import BaseModel

class LaptopInput(BaseModel):
    Company: str
    Product: str
    TypeName: str
    Inches: float
    ScreenResolution: str
    Cpu: str
    Ram: int
    Memory: str
    Gpu: str
    OpSys: str
    Weight: float