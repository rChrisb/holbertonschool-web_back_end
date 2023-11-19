/* eslint-disable */

class Currency {
  constructor(code, name) {
    this._code = this._validateString(code, "code");
    this._name = this._validateString(name, "name");
  }

  get code() {
    return this._code;
  }

  set code(value) {
    this._code = this._validateString(value, "code");
  }

  get name() {
    return this._name;
  }

  set name(value) {
    this._name = this._validateString(value, "name");
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }

  _validateString(value, attribute) {
    if (typeof value !== "string") {
      throw new TypeError(`${attribute} must be a string`);
    }
    return value;
  }
}

export default Currency;
