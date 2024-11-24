import Proyect from "./Proyect";

export default function ProyectAdmin() {

    const subscriptionStatus = false

    return (
        <>
            <div className=" bg-gray-300 shadow-xl mt-[10px] w-[600px] mx-auto rounded-xl p-2 flex flex-col">
                <div className="flex justify-around" >
                    <h3 className="text-gray-600 font-bold">USER</h3>
                    {
                        subscriptionStatus
                            ? <h3 className="text-gray-600 font-bold flex">Subcription: <h3 className="text-green-600 ml-[10px] font-bold">Active</h3></h3>
                            : <h3 className="text-gray-600 font-bold flex">Subcription: <h3 className="text-red-600 ml-[10px] font-bold">Inactive</h3></h3>
                    }
                    {
                        subscriptionStatus
                            ? ""
                            : <button className=" bg-gray-500 hover:bg-slate-600 text-white rounded-xl p-2 font-bold">Get Subscription</button>
                    }
                </div>

                <Proyect />

                <button className="bg-slate-400 hover:bg-slate-600 rounded-lg h-{30px} w-[100px] mx-auto">Create New Proyect</button>
            </div>
        </>
    )
}