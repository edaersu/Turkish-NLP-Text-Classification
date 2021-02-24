import 'dart:html';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:labeling/test_page/test_view_model.dart';

class TestView extends TestViewModel {
  Storage storage;
  @override
  Widget build(BuildContext context) {
    TextEditingController controller = TextEditingController();
    String state;
    Future<Directory> _appDocDir;
    return Scaffold(
      body: Center(
        child: Text("vbnmöç"),
      ),
    );
  }
}
