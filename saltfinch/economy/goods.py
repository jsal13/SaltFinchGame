from attrs import define, field

@define
class Good:
    name: str
    base_price: float
    volatility: float  # How much the price can fluctuate day to day
    current_price: float = field(default=0.0, init=False)

    @classmethod
    def create(cls, name: str, base_price: float, volatility: float) -> "Good":
        good_class: "Good" = cls(
            name=name,
            base_price=base_price,
            volatility=volatility
        )
        good_class.current_price = good_class.base_price
        return good_class
        