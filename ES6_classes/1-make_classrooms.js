import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const arr = [];
  arr.push(new ClassRoom(19));
  arr.push(new ClassRoom(20));
  arr.push(new ClassRoom(34));
  return arr;
}
