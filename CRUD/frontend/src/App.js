import React, { useEffect, useState } from "react";
import axios from "axios";
import './App.css';

export default function App() {
  const [usuarios, setUsuarios] = useState([]);
  const [form, setForm] = useState({ nome: "", idade: "", telefone: "" });
  const [idBusca, setIdBusca] = useState("");
  const [editId, setEditId] = useState(null);
  const api = "http://localhost:5000";

  useEffect(() => {
    listarTodos();
  }, []);

  const listarTodos = async () => {
    const res = await axios.get(`${api}/listar-todos`);
    setUsuarios(res.data);
  };

  const buscarPorId = async () => {
    try {
      const res = await axios.get(`${api}/listar/id/${idBusca}`);
      setUsuarios(res.data);
    } catch (err) {
      alert("Usuário não encontrado");
    }
  };

  const adicionar = async () => {
    await axios.post(`${api}/add`, form);
    setForm({ nome: "", idade: "", telefone: "" });
    listarTodos();
  };

  const deletar = async (id) => {
    await axios.delete(`${api}/deletar/id/${id}`);
    listarTodos();
  };

  const editar = (usuario) => {
    setForm({ nome: usuario[1], idade: usuario[2], telefone: usuario[3] });
    setEditId(usuario[0]);
  };

  const atualizar = async () => {
    await axios.put(`${api}/update/id/${editId}`, form);
    setEditId(null);
    setForm({ nome: "", idade: "", telefone: "" });
    listarTodos();
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-sky-100 to-white p-6">
      <div className="max-w-4xl mx-auto bg-white rounded-2xl shadow-xl p-6">
        <h1 className="text-4xl font-bold text-center text-blue-600 mb-6">
          Gerenciamento de Usuários
        </h1>

        {/* Busca */}
        <div className="flex flex-col md:flex-row gap-3 mb-6">
          <input
            className="border border-gray-300 p-3 rounded-lg flex-1"
            placeholder="ID para buscar"
            value={idBusca}
            onChange={(e) => setIdBusca(e.target.value)}
          />
          <button
            onClick={buscarPorId}
            className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition"
          >
            Buscar por ID
          </button>
          <button
            onClick={listarTodos}
            className="bg-gray-500 hover:bg-gray-600 text-white px-4 py-2 rounded-lg transition"
          >
            Listar Todos
          </button>
        </div>

        {/* Formulário */}
        <div className="flex flex-col md:flex-row gap-3 mb-6">
          <input
            className="border border-gray-300 p-3 rounded-lg flex-1"
            placeholder="Nome"
            value={form.nome}
            onChange={(e) => setForm({ ...form, nome: e.target.value })}
          />
          <input
            className="border border-gray-300 p-3 rounded-lg flex-1"
            placeholder="Idade"
            value={form.idade}
            onChange={(e) => setForm({ ...form, idade: e.target.value })}
          />
          <input
            className="border border-gray-300 p-3 rounded-lg flex-1"
            placeholder="Telefone"
            value={form.telefone}
            onChange={(e) => setForm({ ...form, telefone: e.target.value })}
          />
          {editId ? (
            <button
              onClick={atualizar}
              className="bg-yellow-500 hover:bg-yellow-600 text-white px-4 py-2 rounded-lg transition"
            >
              Atualizar
            </button>
          ) : (
            <button
              onClick={adicionar}
              className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg transition"
            >
              Adicionar
            </button>
          )}
        </div>

        {/* Lista de Usuários */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {usuarios.map((u, idx) => (
            <div
              key={idx}
              className="bg-gray-100 p-4 rounded-xl shadow-sm border border-gray-200 flex flex-col justify-between"
            >
              <div>
                <p className="text-gray-800">
                  <strong>ID:</strong> {u[0]}
                </p>
                <p className="text-gray-800">
                  <strong>Nome:</strong> {u[1]}
                </p>
                <p className="text-gray-800">
                  <strong>Idade:</strong> {u[2]}
                </p>
                <p className="text-gray-800">
                  <strong>Telefone:</strong> {u[3]}
                </p>
              </div>
              <div className="flex gap-2 mt-4">
                <button
                  onClick={() => editar(u)}
                  className="bg-yellow-400 hover:bg-yellow-500 px-3 py-1 rounded text-sm"
                >
                  Editar
                </button>
                <button
                  onClick={() => deletar(u[0])}
                  className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-sm"
                >
                  Deletar
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
