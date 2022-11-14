# Copyright 2021 Agnostiq Inc.
#
# This file is part of Covalent.
#
# Licensed under the GNU Affero General Public License 3.0 (the "License").
# A copy of the License may be obtained with this software package or at
#
#      https://www.gnu.org/licenses/agpl-3.0.en.html
#
# Use of this file is prohibited except in compliance with the License. Any
# modifications or derivative works of this file must retain this copyright
# notice, and modified files must contain a notice indicating that they have
# been altered from the originals.
#
# Covalent is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the License for more details.
#
# Relief from the License may be granted by purchasing a commercial license.

"""Electrons Schema """

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, func

from covalent_ui.api.v1.database.config.db import Base


class Electron(Base):
    """Electron

    Attributes:
        id: primary key id
        parent_lattice_id: id of the lattice containing this electron
        transport_graph_node_id: id of the node in the context of a transport graph
        type: node type
        name: node name
        status: Execution status of the node
        storage_type: Storage backend type for data files ("local", "s3")
        storage_path: Bucket name (dispatch_id)
        function_filename: Name of the file containing the serialized function
        function_string_filename: Name of the file containing the function string
        executor_filename: Name of the file containing the serialized executor
        error_filename: Name of the file containing an error message for the electron
        results_filename: Name of the file containing the serialized output
        value_filename: Name of the file containing the serialized parameter (for parameter nodes)
        attribute_name: Electron attribute name (for attribute nodes)
        key: For generated and subscript nodes
        stdout_filename: Name of the file containing standard output generated by the task
        stderr_filename: Name of the file containing standard error generated by the task
        deps_filename: Name of the file containing depends instances of DepsBash and DepsPip
        call_before_filename: Name of the file containing list of DepsCall objects
        call_after_filename : Name of the file containing list of DepsCall objects
        error_filename: Name of the file containing execution information generated at runtime
        is_active: Status of the record, 1: active and 0: inactive
        created_at: created timestamp
        updated_at: updated timestamp
        started_at: started timestamp
        completed_at: completed timestamp
    """

    __tablename__ = "electrons"
    id = Column(Integer, primary_key=True)

    # id of the lattice containing this electron
    parent_lattice_id = Column(Integer, ForeignKey("lattices.id"), nullable=False)

    # id of the node in the context of a transport graph
    transport_graph_node_id = Column(Integer, nullable=False)

    # Node type
    type = Column(String(24), nullable=False)

    # Node name
    name = Column(Text, nullable=False)

    # Execution status of the node
    status = Column(String(24), nullable=False)

    # Storage backend type for data files ("local", "s3")
    storage_type = Column(Text)

    # Bucket name (dispatch_id)
    storage_path = Column(Text)

    # Name of the file containing the serialized function
    function_filename = Column(Text)

    # Name of the file containing the function string
    function_string_filename = Column(Text)

    # Short name describing the executor ("local", "dask", etc)
    executor = Column(Text)

    # Name of the file containing the serialized executor data
    executor_data_filename = Column(Text)

    # name of the file containing the serialized output
    results_filename = Column(Text)

    # Name of the file containing the serialized parameter (for parameter nodes)
    value_filename = Column(Text)

    # Name of the file containing standard output generated by the task
    stdout_filename = Column(Text)

    # Name of the file containing the electron execution dependencies
    deps_filename = Column(Text)

    # Name of the file containing the functions that are called before electron execution
    call_before_filename = Column(Text)

    # Name of the file containing the functions that are called before electron execution
    call_after_filename = Column(Text)

    # Name of the file containing standard error generated by the task
    stderr_filename = Column(Text)

    # Name of the file containing errors generated by the task runner or executor
    error_filename = Column(Text)

    # Name of the column which signifies soft deletion of the electrons corresponding to a lattice
    is_active = Column(Boolean, nullable=False, default=True)

    # Timestamps
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, onupdate=func.now(), server_default=func.now())
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
