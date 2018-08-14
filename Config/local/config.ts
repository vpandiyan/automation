export interface BackEnd {
	host: string;
	path: string;
}

export class Constants {
	username: string = 'userName';
	deviceToken = '';
	token: string = "token";
	version: any = 'v1.0';
	categoriesJson: string = "categories"
	myRequestJson: string = "myRequests";
	pendingJson: string = "pendings";
	jobJson: string = "jobs";
	imgJson: string = "imgJson";
	firbaseProjectId: string = "cryotos-cmms";
	locationRadius: string = "LocationRadius";
	timeout: number = 15000;
	draftNewReqs: string = "draftNewReqs";
	routeDraft: string = "routeDrafts";
	ackDraft: string = 'ackDraft';
	reqDetailJson: string = "reqDetailJson";
	userList: string = "userList";
	msgNotificationJson: string = "msgNotificationJson";
	calendarJson: string = "calendarJson";
	imageUpload: string = "imageUpload";
	checkIn: string = "checkIn";
	rejectCommentLength: Number = 200;
	assetListJson: string = "asset";
	isAsset: boolean = false;
	isCategory: boolean = true;
	paginationCount: string = "10";
	canAddCustomer: boolean = true;
	canReschedule: boolean = false;
	isFirestoreEnabled: boolean = true;
	setting: any = {
		name: "Cryotos",
		LocationRadius: 100,
		RecordCount: 5,
		Language: "en",
		timeout: 5000,
		isAsset: false,
		isCategory: false,
		pushPopup: true,
		CategoryTitle: {
			A: "Choose Category",
			B: "Choose Subcategory",
			C: "Choose Subcategory",
			D: "Choose Subcategory"
		},
		LocationTitle: {
			A: "Choose Location",
			B: "Choose Sublocation"
		}
	};
}

export class CatQuestions {
	A: string = "Choose Category";
	B: string = "Choose Subcategory";
	C: string = "Choose Subcategory";
	D: string = "Choose Subcategory";
}

export class LocQuestions {
	A: string = "Choose Location";
	B: string = "Choose Sublocation";

}

export class CustomerQuestions {
	A: String = 'Select Customer';
	B: String = 'Add Customer';
}

export const fireBaseConfig = {
	// Cryotos Test
	apiKey: "AIzaSyDLW-ugqSHHDmttpdEn-TMNMyw-F8a5EJw",
    authDomain: "piqotech-qa.firebaseapp.com",
    databaseURL: "https://piqotech-qa.firebaseio.com",
    projectId: "piqotech-qa",
    storageBucket: "piqotech-qa.appspot.com",
    messagingSenderId: "361929196857"
}


class AppConfig {
	name: string = 'Cryotos';
	backend: BackEnd = {
		host: 'http://111.93.240.74:9200',
		path: '/',
	};
	constants: Constants = new Constants();
	catQuestions: CatQuestions = new CatQuestions();
	locQuestions: LocQuestions = new LocQuestions();
	customerQuestions: CustomerQuestions = new CustomerQuestions();

	constructor() { }
}

export let Config = new AppConfig()
