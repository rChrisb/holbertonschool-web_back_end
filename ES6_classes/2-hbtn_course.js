/* eslint-disable */

class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this._validateString(name, "name");
    this._length = this._validateNumber(length, "length");
    this._students = this._validateStudents(students);
  }

  get name() {
    return this._name;
  }

  set name(value) {
    this._name = this._validateString(value, "name");
  }

  get length() {
    return this._length;
  }

  set length(value) {
    this._length = this._validateNumber(value, "length");
  }

  get students() {
    return this._students;
  }

  set students(value) {
    this._students = this._validateStudents(value);
  }

  _validateString(value, attribute) {
    if (typeof value !== "string") {
      throw new TypeError(`${attribute} must be a string`);
    }
    return value;
  }

  _validateNumber(value, attribute) {
    if (typeof value !== "number") {
      throw new TypeError(`${attribute} must be a number`);
    }
    return value;
  }

  _validateStudents(students) {
    if (
      !Array.isArray(students) ||
      !students.every((student) => typeof student === "string")
    ) {
      throw new TypeError("students must be an array of strings");
    }
    return students;
  }
}

export default HolbertonCourse;
