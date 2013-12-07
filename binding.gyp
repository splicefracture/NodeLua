{
  "targets": [
    {
      "target_name": "nodelua",
      "variables": {
        "lua_include": "/usr/local/openresty/luajit/include/luajit-2.0/",
	"lua_version": "5.1.4"
        },
      "sources": [
        "src/utils.cc",
        "src/luastate.cc",
	"src/nodelua.cc"
	],
      "include_dirs": [
        "<@(lua_include)",
        ],
      "libraries": [
        "<!(pkg-config --libs-only-l --silence-errors lua || pkg-config --libs-only-l --silence-errors lua5.1)",
        "-ldl"
	]
    }
  ]
}
