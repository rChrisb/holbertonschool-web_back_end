class Building {
  constructor(sqft) {
    this._sqft = this._validateNumber(sqft, "sqft");
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    throw new Error(
      "Class extending Building must override evacuationWarningMessage"
    );
  }

  _validateNumber(value, attribute) {
    if (typeof value !== "number" || isNaN(value)) {
      throw new TypeError(`${attribute} must be a valid number`);
    }
    return value;
  }
}

export default Building;
