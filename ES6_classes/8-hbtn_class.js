export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  [Symbol.toPrimitive](dataType) {
    if (dataType === 'string') {
      return `${this._location}`;
    }
    if (dataType === 'number') {
      return `${this._size}`;
    }
    return `${this._location}`;
  }
}
