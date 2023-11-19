import Currency from "./3-currency.js";

class Pricing {
  constructor(amount, currency) {
    this._amount = this._validateNumber(amount, "amount");
    this._currency = this._validateCurrency(currency, "currency");
  }

  get amount() {
    return this._amount;
  }

  set amount(value) {
    this._amount = this._validateNumber(value, "amount");
  }

  get currency() {
    return this._currency;
  }

  set currency(value) {
    this._currency = this._validateCurrency(value, "currency");
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }

  _validateNumber(value, attribute) {
    if (typeof value !== "number" || isNaN(value)) {
      throw new TypeError(`${attribute} must be a valid number`);
    }
    return value;
  }

  _validateCurrency(value, attribute) {
    if (!(value instanceof Currency)) {
      throw new TypeError(`${attribute} must be an instance of Currency`);
    }
    return value;
  }
}

export default Pricing;
