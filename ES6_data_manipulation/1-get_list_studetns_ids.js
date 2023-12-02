export default function getListStudentIds(ids) {
  if (Array.isArray(ids)) {
    return ids.map((student) => student.id);
  }
  return [];
}
