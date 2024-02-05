import '/auth/firebase_auth/auth_util.dart';
import '/backend/backend.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import 'add_first_car_widget.dart' show AddFirstCarWidget;
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';

class AddFirstCarModel extends FlutterFlowModel<AddFirstCarWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();
  // State field(s) for model widget.
  FocusNode? modelFocusNode;
  TextEditingController? modelController;
  String? Function(BuildContext, String?)? modelControllerValidator;
  // State field(s) for plateNumber widget.
  FocusNode? plateNumberFocusNode;
  TextEditingController? plateNumberController;
  String? Function(BuildContext, String?)? plateNumberControllerValidator;
  // State field(s) for vin widget.
  FocusNode? vinFocusNode;
  TextEditingController? vinController;
  String? Function(BuildContext, String?)? vinControllerValidator;
  // State field(s) for TextField widget.
  FocusNode? textFieldFocusNode;
  TextEditingController? textController4;
  String? Function(BuildContext, String?)? textController4Validator;

  /// Initialization and disposal methods.

  void initState(BuildContext context) {}

  void dispose() {
    unfocusNode.dispose();
    modelFocusNode?.dispose();
    modelController?.dispose();

    plateNumberFocusNode?.dispose();
    plateNumberController?.dispose();

    vinFocusNode?.dispose();
    vinController?.dispose();

    textFieldFocusNode?.dispose();
    textController4?.dispose();
  }

  /// Action blocks are added here.

  /// Additional helper methods are added here.
}
