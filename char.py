class Karakter:
    ras = "Manusia"
    
    def __init__(self, nama: str, health: int, damage: int):
        self.nama = nama
        self.health = health
        self.health_max = health
        self.damage = damage

    def serang(self, target) -> None:
        target.health -= self.damage
        target.health = max(target, 0)