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
	isAsset: boolean = true;
	isCategory: boolean = false;
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
	// Cryotos Lincoln
	apiKey: "AIzaSyApULn4PYAb6wKKHRczAieoOH_cfvzkNgE",
    authDomain: "cryotos-lincoln.firebaseapp.com",
    databaseURL: "https://cryotos-lincoln.firebaseio.com",
    projectId: "cryotos-lincoln",
    storageBucket: "cryotos-lincoln.appspot.com",
    messagingSenderId: "770793890981"
}


class AppConfig {
	name: string = 'Cryotos';
	backend: BackEnd = {
		host: 'http://lincoln.cryotos.com:9100',
		path: '/',
	};
	constants: Constants = new Constants();
	catQuestions: CatQuestions = new CatQuestions();
	locQuestions: LocQuestions = new LocQuestions();
	customerQuestions: CustomerQuestions = new CustomerQuestions();

	constructor() { }
}

export let Config = new AppConfig()
