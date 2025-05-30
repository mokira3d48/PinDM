#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
================================================================================
|                  THE PROGRAMMER IN DEBUGE MODE (PinDM)                       |
================================================================================

                                Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""

__version__ = '0.1.0'
__author__ = 'Dr Mokira'

import os
import json
import base64
import logging
from argparse import ArgumentParser, FileType

from flask import Flask, render_template

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    # format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    format="%(name)s - \033[96m%(levelname)s\033[0m - %(message)s",
    handlers=[
        logging.FileHandler("pindm.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('PinDM')
app = Flask(__name__)


class Exec:
    """
    Proposal definition
    -------------------

    :arg lineno: The number the code line
    :arg values: The dictionary of variable names, each associated
      with its value

    :type lineno: int
    :type values: object
    """
    def __init__(self, lineno, **values):
        self.lineno = lineno
        self.__dict__.update(**values)

    @property
    def variables(self):
        """
        :returns: Data dict of values proposed for each variable
        :rtype: typing.Dict[str, object]
        """
        return {
            key:val for key, val in self.__dict__.items() if key != "lineno"}


def _exec_data_iteration(src):
    columns = list(src.values())

    # Length of one column represents number of rows
    num_rows = len(columns[0])

    for i in range(num_rows):
        row_data = {}
        for var_name in src:
            row_data[var_name] = src[var_name][i]
        yield row_data


class SequenceOfExec(list):
    """
    Sequence of execution

    :arg var_names: The list of variable names
    :type var_names: list of str
    """
    def __init__(self, var_names):
        super().__init__([])
        if not var_names:
            raise ValueError("Unexpected a empty list of variable names")
        self.var_names = var_names
        self.max_string_length = -float("inf")

    def _reg_max_string_length(self, exec_instance):
        for value in exec_instance.variables.values():
            str_length = len(value)
            if str_length > self.max_string_length:
                self.max_string_length = str_length

    def append(self, elem):
        """
        :param elem: The new instance of Exec
        :type elem: `Exec`
        """
        # for var_name in self.var_names:
        #     if var_name in elem.variables:
        #         continue
        self._reg_max_string_length(elem)
        super().append(elem)

    def insert(self, __index, __object):
        """
        :param __index: The index of the new execution
        :param __object: The instance of new Exec

        :type __index: `int`
        :type __object: `Exec`
        """
        # for var_name in self.var_names:
        #     if var_name in __object.variables:
        #         continue
        #     __object.variables[var_name] = None
        self._reg_max_string_length(__object)
        super().insert(__index, __object)

    def __setitem__(self, key, value):
        self._reg_max_string_length(value)
        super().__setitem__(key, value)

    def __contains__(self, item):
        search_lineno = item.lineno
        for elem in self:
            if search_lineno == elem.lineno:
                return True
        return False

    def load_state_dict(self, src):
        """
        Method to load sequence of executions from dictionary

        :param src: The instance of dictionary that contents name of columns
          mapped with lists of string representing the rows
        :type src: dict of list
        """
        exec_data_iter = _exec_data_iteration(src)
        for exec_data in exec_data_iter:
            if 'lineno' not in exec_data:
                raise ValueError("The lineno value is missing")
            lineno = exec_data['lineno']
            del exec_data['lineno']
            exec_inst = Exec(lineno, **exec_data)
            self.append(exec_inst)


def test_sequence_of_chaine():
    seq_of_ex = SequenceOfExec(["var1", "var2", "var3"])
    exec1 = Exec(12, var3="23", var1="\"coca21\"")
    exec2 = Exec(13, var2="23", var3="\"coca1\"")
    exec3 = Exec(14, var1="23", var2="\"coca\"")

    seq_of_ex.append(exec1)
    seq_of_ex.append(exec2)
    seq_of_ex.append(exec3)

    assert seq_of_ex.max_string_length == 8
    assert len(seq_of_ex) == 3


class Exocode:
    """
    The exocode represents an exercise and its solution. Each exercise
    can be saved and loaded from a binary file.

    :arg language: The programming language used in source code
    :arg source_code: The string of the source code written
      in the programming language specified
    :arg target_vars: The target variable whose values will be monitored
    :arg solution: The expected debugging solution for this source code

    :type language: `str`
    :type source_code: `str`
    :type solution: `SequenceOfExec`
    """
    def __init__(self, language, source_code, target_vars, solution):
        self.language = language.strip()
        self.source_code = source_code.strip()
        self.target_vars = target_vars
        self.solution = solution

    class FileLoadError(Exception):
        """
        When an error occurs while loading the exocode file.
        """
        ...

    @classmethod
    def load(cls, input_file):
        """
        Static method to load exocode from file

        :param input_file: The file that contents the exocode data
        :returns: An instance of exocode carrying the information
          loaded from file.

        :type input_file: `str` | typing.BinaryIO
        :rtype: Exocode
        """
        try:
            f = (
                input_file if not isinstance(input_file, str)
                else open(input_file, mode='rb'))

            encoded_content = f.read()
            f.close()

            decoded_content = base64.b64decode(encoded_content)
            jsonify_content = decoded_content.decode(encoding='utf-8')

            data = json.loads(jsonify_content)
            language = data.get('language')
            source_code = data.get('source_code')
            target_vars = data.get('target_vars')

            solution = data.get('solution')
            sequence_of_exec = SequenceOfExec(target_vars)
            sequence_of_exec.load_state_dict(solution)

            instance = cls(
                language, source_code, target_vars, sequence_of_exec)

            return instance
        except Exception as e:
            message = f"{e.__class__.__name__}: {e.args[0]}"
            raise cls.FileLoadError(message)

    def source_code_str(self):
        """
        This function returns the source code in formatted string

        :rtype: `str`
        """
        string = ''
        sc_lines = self.source_code.split('\n')
        for i, line in enumerate(sc_lines):
            string += "  " + f"\033[91m{i+1:02d}\033[0m {line}\n"
        return string

    def target_vars_str(self):
        """
        This function returns the list of target variables
        in formatted string

        :rtype: `str`
        """
        string = ''
        for i, varname in enumerate(self.target_vars):
            string += "  " + f"{i + 1}. {varname}\n"
        return string

    def __str__(self):
        return self.source_code_str() + "\n\n" + self.target_vars_str()


def validation(proposal, solution):
    """
    Function to validate proposal according solution

    :param proposal: The solution proposed by the programmer
    :param solution: The solution expected
    :returns: The calculated metric of appreciation.

    :type proposal:`SequenceOfExec`
    :type solution: `SequenceOfExec`
    :rtype: dict
    """
    precision = 0.0
    recall = 0.0

    for s in solution:
        if s in proposal:
            recall += 1
    for p, s in zip(proposal, solution):
        if p.lineno != s.lineno:
            continue
        all_var_are_equals = True
        for var_name in s.variables:
            if p.variables[var_name] == s.variables[var_name]:
                continue
            all_var_are_equals = False
        if all_var_are_equals:
            precision += 1

    max_length = max(len(proposal), len(solution))
    precision = precision / max_length
    recall = recall / len(solution)
    f1_score = 2 * precision * recall / (precision + recall)
    return {
        'precision': precision,
        'recall': recall,
        'f1_score': f1_score}


def test_validation_function():
    solution = SequenceOfExec(["var1", "var2", "var3"])
    solution.append(Exec(12, var3="23", var1="\"coca21\""))
    solution.append(Exec(13, var2="23", var3="\"coca1\""))
    solution.append(Exec(14, var1="23", var2="\"coca\""))

    proposal = SequenceOfExec(["var1", "var2", "var3"])
    proposal.append(Exec(12, var3="23", var1="\"coca21\""))
    proposal.append(Exec(13, var2="23", var3="\"coca1\""))
    proposal.append(Exec(14, var1="23", var2="\"coca\""))

    results = validation(proposal, solution)
    assert results['precision'] == 1.0
    assert results['recall'] == 1.0
    assert results['f1_score'] == 1.0

    proposal = SequenceOfExec(["var1", "var2", "var3"])
    proposal.append(Exec(10, var3="23", var1="\"coca21\""))
    proposal.append(Exec(13, var2="23", var3="\"coca1\""))
    proposal.append(Exec(14, var1="23", var2="\"coca\""))

    results = validation(proposal, solution)
    assert results['precision'] == 0.6666666666666666
    assert results['recall'] == 0.6666666666666666
    assert results['f1_score'] == 0.6666666666666666


def get_exocode_example():
    language = "C"
    source_code = """
#include <stdlib.h>
#include <stdio.h>


void main(int argc, char** argv) {
    int age = 0;
    printf("Hello world!");
    printf("Enter your age.");
    scanf("%d", &age);
    
    printf("Your age is %d years old.", age);
    return 0;
}
"""
    target_vars = ['i']
    return Exocode(
        language, source_code, target_vars, SequenceOfExec(target_vars))


def get_menu():
    string = """
+-----------------------------------------------------------------------------+
|                             PinDM Menu                                      |
+-----------------------------------------------------------------------------+
|                                                                             |
|        * "i" or "insert" -> INSERT NEW;                                     |
|        * "s" or "select" -> SHOW INDEXED LINE;                              |
|        * "u" or "update" -> UPDATE INDEXED LINE;                            |
|        * "d" or "delete" -> DELETE INDEXED LINE.                            |
|                                                                             |
+-----------------------------------------------------------------------------+
"""
    return string


def clt():
    """
    Function to clear terminal
    """
    os.system("clear")


def describe_exocode(args):
    """
    Function to describe exocode given
    """
    exocode = get_exocode_example()
    memu_str = get_menu()
    clt()
    print(memu_str)
    print(f"\033[42m\033[91m{exocode.language.upper()} \033[0m CODE:\n")
    print(exocode.source_code_str())
    print("\n\n")
    print("List of target variables to monitor:")
    print(exocode.target_vars_str())


def train_on_exocode(args):
    """
    Function to run training process on given exocode
    """
    ...


features = {"describe": describe_exocode,
            "train": train_on_exocode}


def get_argument():
    """
    Function to parse command line arguments

    :rtype: argparse.Namespace
    """
    parser = ArgumentParser(prog="PinDM")
    # parser.add_argument("action", type=str, choices=list(features.keys()))
    # parser.add_argument(
    #     "exocode", type=FileType(mode='rb'),
    #     help="Exocode file")
    parser.add_argument("-o", "--output", type=str, default="outputs")
    parser.add_argument('--host', type=str, default='0.0.0.0')
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()
    return args


def main():
    """
    Main function to run this program
    """
    args = get_argument()

    @app.route('/')
    def show_training_page():
        """
        Render the web page of training
        """
        return render_template('index.html')

    # action = args.action
    # function = features.get(action)
    # if not function:
    #     print("This feature is not supported yet.")
    #     exit(0)
    # function(args)

    # app.run(debug=True, host='0.0.0.0', port=5000)
    app.run(host=args.host, port=args.port)


if __name__ == '__main__':
    try:
        main()
        exit(0)
    except KeyboardInterrupt:
        print("Good bye! I hope, see you next time.")
        exit(125)
