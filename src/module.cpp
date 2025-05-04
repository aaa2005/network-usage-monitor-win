#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <regex>
#include <cstdio>
#include <memory>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;


struct NetworkInterface
{
    std::string name;
    int bytesIn;
    int bytesOut;
};


std::vector<NetworkInterface> NetUsage() {
    std::string cmd = "netsh interface ipv4 show subinterface";  
    std::string output ="";
    char buffer[128];

    std::unique_ptr<FILE, decltype(&_pclose)> pipe(_popen(cmd.c_str(), "r"), _pclose);

    

    while(fgets(buffer, sizeof(buffer), pipe.get()) != nullptr){
        output += buffer;
    }

    std::regex pattern(R"(\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(.+))");
    std::smatch match;
    std::vector<NetworkInterface> interfaces;


    std::stringstream ss(output);
    std::string line;


    while (std::getline(ss, line)){

        if (std::regex_match(line, match, pattern)) {
            std::string interfaceName = match[5];
            int bytesIn = std::stoi(match[3]);
            int bytesOut = std::stoi(match[4]);
            if (interfaceName == "Ethernet" || interfaceName == "Wi-Fi" || interfaceName == "Cellular"){
                interfaces.push_back({interfaceName, bytesIn, bytesOut});
            }
        }
    }


    return interfaces;
}


PYBIND11_MODULE(netusage, m){
    py::class_<NetworkInterface>(m,"Interface")
        .def_readwrite("name", &NetworkInterface::name)
        .def_readwrite("byteIn", &NetworkInterface::bytesIn)
        .def_readwrite("byteOut", &NetworkInterface::bytesOut);
    m.def("usage_info", &NetUsage);
}
