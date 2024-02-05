import 'dart:async';

import 'package:collection/collection.dart';

import '/backend/schema/util/firestore_util.dart';
import '/backend/schema/util/schema_util.dart';

import 'index.dart';
import '/flutter_flow/flutter_flow_util.dart';

class VehiclesRecord extends FirestoreRecord {
  VehiclesRecord._(
    DocumentReference reference,
    Map<String, dynamic> data,
  ) : super(reference, data) {
    _initializeFields();
  }

  // "imageLink" field.
  String? _imageLink;
  String get imageLink => _imageLink ?? '';
  bool hasImageLink() => _imageLink != null;

  // "model" field.
  String? _model;
  String get model => _model ?? '';
  bool hasModel() => _model != null;

  // "plateNumber" field.
  String? _plateNumber;
  String get plateNumber => _plateNumber ?? '';
  bool hasPlateNumber() => _plateNumber != null;

  // "vin" field.
  String? _vin;
  String get vin => _vin ?? '';
  bool hasVin() => _vin != null;

  // "uid" field.
  String? _uid;
  String get uid => _uid ?? '';
  bool hasUid() => _uid != null;

  void _initializeFields() {
    _imageLink = snapshotData['imageLink'] as String?;
    _model = snapshotData['model'] as String?;
    _plateNumber = snapshotData['plateNumber'] as String?;
    _vin = snapshotData['vin'] as String?;
    _uid = snapshotData['uid'] as String?;
  }

  static CollectionReference get collection =>
      FirebaseFirestore.instance.collection('vehicles');

  static Stream<VehiclesRecord> getDocument(DocumentReference ref) =>
      ref.snapshots().map((s) => VehiclesRecord.fromSnapshot(s));

  static Future<VehiclesRecord> getDocumentOnce(DocumentReference ref) =>
      ref.get().then((s) => VehiclesRecord.fromSnapshot(s));

  static VehiclesRecord fromSnapshot(DocumentSnapshot snapshot) =>
      VehiclesRecord._(
        snapshot.reference,
        mapFromFirestore(snapshot.data() as Map<String, dynamic>),
      );

  static VehiclesRecord getDocumentFromData(
    Map<String, dynamic> data,
    DocumentReference reference,
  ) =>
      VehiclesRecord._(reference, mapFromFirestore(data));

  @override
  String toString() =>
      'VehiclesRecord(reference: ${reference.path}, data: $snapshotData)';

  @override
  int get hashCode => reference.path.hashCode;

  @override
  bool operator ==(other) =>
      other is VehiclesRecord &&
      reference.path.hashCode == other.reference.path.hashCode;
}

Map<String, dynamic> createVehiclesRecordData({
  String? imageLink,
  String? model,
  String? plateNumber,
  String? vin,
  String? uid,
}) {
  final firestoreData = mapToFirestore(
    <String, dynamic>{
      'imageLink': imageLink,
      'model': model,
      'plateNumber': plateNumber,
      'vin': vin,
      'uid': uid,
    }.withoutNulls,
  );

  return firestoreData;
}

class VehiclesRecordDocumentEquality implements Equality<VehiclesRecord> {
  const VehiclesRecordDocumentEquality();

  @override
  bool equals(VehiclesRecord? e1, VehiclesRecord? e2) {
    return e1?.imageLink == e2?.imageLink &&
        e1?.model == e2?.model &&
        e1?.plateNumber == e2?.plateNumber &&
        e1?.vin == e2?.vin &&
        e1?.uid == e2?.uid;
  }

  @override
  int hash(VehiclesRecord? e) => const ListEquality()
      .hash([e?.imageLink, e?.model, e?.plateNumber, e?.vin, e?.uid]);

  @override
  bool isValidKey(Object? o) => o is VehiclesRecord;
}
